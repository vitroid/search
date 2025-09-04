import json
import sqlite3
import time
from logging import getLogger, basicConfig, INFO, DEBUG
import re
import os
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

# グローバル変数を削除して、各関数内でDB接続を行う
# hardcoded

app = FastAPI()

basicConfig(level=DEBUG)   # CORS デバッグ用

# 開発/本番環境の判定
IS_DEVELOPMENT = os.getenv("ENVIRONMENT", "development") == "development"

if IS_DEVELOPMENT:
    # 開発環境: すべてのオリジンを許可（credentials無効）
    origins = ["*"]
    allow_credentials = False
    print("🚧 開発モード: すべてのオリジンを許可")
else:
    # 本番環境: 特定のオリジンのみ許可
    origins = [
        # ローカル開発環境
        "http://localhost:8080",
        "http://127.0.0.1:8080",
        # 本番環境
        "http://sakutai.net",
        "https://sakutai.net",
        # その他必要なオリジン
        "http://localhost",
        "http://127.0.0.1",
    ]
    allow_credentials = True
    print("🔒 本番モード: 特定オリジンのみ許可")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=allow_credentials,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# グローバルエラーハンドラー
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """グローバルエラーハンドラー - CORSヘッダーを確実に返す"""
    print(f"🚨 サーバーエラー: {exc}")
    print(f"🔗 リクエストURL: {request.url}")
    print(f"🌐 オリジン: {request.headers.get('origin', 'なし')}")
    
    # CORSヘッダーを手動で設定
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "*",
    }
    
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error", "detail": str(exc)},
        headers=headers
    )


def init_database(cursor):
    """データベースのテーブルを初期化する"""
    # votesテーブル: ユーザーの投票データ
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS votes (
            id TEXT,
            favs TEXT,
            timestamp REAL
        )
    """)
    
    # 既存テーブルのマイグレーション: created_at → timestamp
    try:
        # created_atカラムが存在する場合、timestampカラムを追加
        cursor.execute("SELECT created_at FROM votes LIMIT 1")
        print("🔄 古いスキーマを検出: created_at → timestamp にマイグレーション中...")
        
        # timestampカラムを追加（存在しない場合）
        cursor.execute("ALTER TABLE votes ADD COLUMN timestamp REAL")
        
        # created_atの値をtimestampにコピー
        cursor.execute("""
            UPDATE votes 
            SET timestamp = strftime('%s', created_at) 
            WHERE timestamp IS NULL
        """)
        
        print("✅ マイグレーション完了")
        
    except Exception as e:
        # created_atカラムが存在しない場合は正常（新しいスキーマ）
        pass
    
    # favsテーブル: 講演の人気ランキング
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favs (
            code TEXT PRIMARY KEY,
            count INTEGER DEFAULT 0
        )
    """)

class Vote(BaseModel):
    id: str
    favs: str


def valid(id: str):
    """idが正常値であるかどうか。"""
    m = re.search(r"^[0-9a-z]{40}$", id)
    return m is not None


def to_dict(favs: str, value: int = 1):
    return {code: value for code in favs.split(",")}


def sub(d1: dict, d2: dict):
    d = d1.copy()
    for key in d2:
        if key not in d:
            d[key] = 0
        d[key] -= d2[key]
    return d


def votes_get(cur, id: str):
    """Votes DBから、idのレコードを読みだす。
    Args:
        cur (_type_): _description_
        id (str): _description_

    Returns:
        _type_: _description_
    """
    for row in cur.execute(
        "SELECT favs FROM votes WHERE id = :id",
        {"id": id},
    ):
        return to_dict(row[0])
    return {}


def votes_delete_expired(cur, expiry: int):
    """Votes DBの、古いレコードを見付けて消す。"""
    logger = getLogger("uvicorn")

    for id, favs in cur.execute(
        "SELECT id, favs FROM votes WHERE timestamp < :expiry",
        {"expiry": expiry},
    ):
        logger.info(f"expire: {id}")
        cur.execute("DELETE FROM votes WHERE id = :id", {"id": id})
        yield to_dict(favs)
    # この書き方は動かないらしい。
    # cur.execute("DELETE FROM votes WHERE id IN (:ids)", {"ids": ",".join(ids)})


def votes_impatient(cur, id):
    """最後の投票から1秒以内かどうかを判定する。"""
    logger = getLogger("uvicorn")

    for row in cur.execute(
        "SELECT id, timestamp FROM votes WHERE id = :id",
        {"id": id},
    ):
        _, ts = row
        return time.time() < float(ts) + 1
    return False


def favs_add(cur, counts: dict):
    for code, value in counts.items():
        if code != "":
            cur.execute(
                "INSERT OR IGNORE INTO favs(code, count) VALUES(:code, 0)",
                {"code": code},
            )
            cur.execute(
                "UPDATE favs SET count = count + :value WHERE code = :code",
                {"value": value, "code": code},
            )


def votes_set(cur, id: str, favs: str):
    cur.execute(
        "INSERT OR IGNORE INTO votes(id, favs, timestamp) VALUES(:id, '', :now)",
        {"id": id, "now": time.time()},
    )
    cur.execute(
        "UPDATE votes SET favs = :favs, timestamp = :now WHERE id = :id",
        {"favs": favs, "id": id, "now": time.time()},
    )


@app.post("/vote")
async def vote(v: Vote):
    """
    ブラウザIDと、好みの講演番号リスト(comma separated)を受けとる
    """
    logger = getLogger("uvicorn")

    if not valid(v.id):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid ID",
            headers={"WWW-Authenticate": "Basic"},
        )

    # DB接続をwith構文で安全に行う
    try:
        with sqlite3.connect("fav.db") as con:
            cur = con.cursor()
            init_database(cur)

            if votes_impatient(cur, v.id):
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail="Busy",
                )

            favs_new = to_dict(v.favs)
            logger.info(f"new vote: {v.id} {v.favs}")
            # すでに登録があるIDなら、まずそちらを読みこんでfavs tableから減算する
            favs_old = votes_get(cur, v.id)
            diff = sub(favs_new, favs_old)
            # favs_add(cur, diff)
            votes_set(cur, v.id, v.favs)

            # expireしたレコードを読みだし、データベースから消す。
            for f in votes_delete_expired(cur, time.time() - 86400 * 7):  # 1 week memory
                diff = sub(diff, f)
            favs_add(cur, diff)

            # con.commit() は自動的に実行される
            logger.info(f"✅ 投票処理完了: {v.id}")
        
    except Exception as e:
        logger.error(f"❌ 投票処理エラー: {e}")
        raise HTTPException(status_code=500, detail=f"Vote processing error: {str(e)}")
    # return query_ranking(id, 100)


@app.get("/top/{id}/{num}")
async def query_ranking(id: str, num: int):
    """
    人気上位n個を返す。
    """
    logger = getLogger("uvicorn")

    if not valid(id):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid ID",
            headers={"WWW-Authenticate": "Basic"},
        )

    # DB接続をwith構文で安全に行う
    try:
        with sqlite3.connect("fav.db") as con:
            cur = con.cursor()
            init_database(cur)

            result = json.dumps(
                dict(
                    cur.execute(
                        "SELECT code, count FROM favs ORDER BY count DESC LIMIT :num",
                        {"num": num},
                    )
                )
            )
            return result
        
    except Exception as e:
        logger.error(f"❌ ランキング取得エラー: {e}")
        raise HTTPException(status_code=500, detail=f"Ranking query error: {str(e)}")
    # /DB


@app.get("/cors-test")
async def cors_test():
    """CORS テスト用エンドポイント"""
    return {
        "message": "CORS テスト成功", 
        "timestamp": time.time(),
        "status": "ok"
    }

@app.get("/w")
async def watch():
    """
    人気上位100個を返す。
    """
    logger = getLogger("uvicorn")

    # DB接続をwith構文で安全に行う
    try:
        with sqlite3.connect("fav.db") as con:
            cur = con.cursor()
            init_database(cur)

            html_content = "<br />".join(
                [
                    f"{value} {key}"
                    for key, value in dict(
                        cur.execute(
                            "SELECT code, count FROM favs ORDER BY count DESC LIMIT 100",
                        )
                    ).items()
                ]
            )
            return HTMLResponse(content=html_content, status_code=200)
        
    except Exception as e:
        logger.error(f"❌ ウォッチページエラー: {e}")
        return HTMLResponse(content=f"エラー: {str(e)}", status_code=500)
    # /DB


def initialize_database_on_startup():
    """サーバー起動時にデータベースを初期化"""
    try:
        # スキーマの不整合がある場合、DBファイルを削除して再作成
        db_path = "fav.db"
        schema_mismatch = False
        
        # 既存DBのスキーマをチェック
        if os.path.exists(db_path):
            try:
                with sqlite3.connect(db_path) as con:
                    cur = con.cursor()
                    # timestampカラムの存在をチェック
                    cur.execute("SELECT timestamp FROM votes LIMIT 1")
            except sqlite3.OperationalError as e:
                if "no such column: timestamp" in str(e):
                    schema_mismatch = True
                    print("🔄 スキーマの不整合を検出: 古いDBファイルを削除して再作成します")
        
        # スキーマが不整合の場合、DBファイルを削除
        if schema_mismatch:
            os.remove(db_path)
            print("🗑️ 古いDBファイルを削除しました")
        
        # データベースを初期化
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            init_database(cur)
            print("✅ データベースが初期化されました")
    except Exception as e:
        print(f"❌ データベース初期化エラー: {e}")

if __name__ == "__main__":
    import argparse
    
    # コマンドライン引数の解析
    parser = argparse.ArgumentParser(description="JSCC API Server")
    parser.add_argument("--https", action="store_true", help="HTTPS モードで起動")
    parser.add_argument("--port", type=int, default=8090, help="ポート番号 (デフォルト: 8090)")
    parser.add_argument("--ssl-cert", type=str, help="SSL証明書ファイルパス")
    parser.add_argument("--ssl-key", type=str, help="SSL秘密鍵ファイルパス")
    
    args = parser.parse_args()
    
    basicConfig(level=DEBUG)
    
    # データベースを初期化
    initialize_database_on_startup()
    
    # ログ設定
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"][
        "fmt"
    ] = "%(asctime)s - %(levelname)s - %(message)s"
    log_config["formatters"]["default"][
        "fmt"
    ] = "%(asctime)s - %(levelname)s - %(message)s"
    
    # HTTPS モード
    if args.https:
        ssl_keyfile = args.ssl_key or os.getenv('SSL_KEYFILE', 'server.key')
        ssl_certfile = args.ssl_cert or os.getenv('SSL_CERTFILE', 'server.crt')
        https_port = 8443 if args.port == 8090 else args.port
        
        print(f"🔒 HTTPS モードで起動中...")
        print(f"   ポート: {https_port}")
        print(f"   証明書: {ssl_certfile}")
        print(f"   秘密鍵: {ssl_keyfile}")
        
        try:
            uvicorn.run(
                app,
                host="0.0.0.0",
                port=https_port,
                ssl_keyfile=ssl_keyfile,
                ssl_certfile=ssl_certfile,
            )
        except FileNotFoundError:
            print("❌ SSL証明書ファイルが見つかりません")
            print("   自己署名証明書を生成: python generate_ssl_cert.py")
        except Exception as e:
            print(f"❌ HTTPS サーバー起動エラー: {e}")
    
    # HTTP モード (デフォルト)
    else:
        print(f"🌐 HTTP モードで起動中...")
        print(f"   ポート: {args.port}")
        
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=args.port,
        )
