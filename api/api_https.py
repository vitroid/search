#!/usr/bin/env python3
"""
HTTPS対応のFastAPI サーバー
"""

import os
import ssl
import uvicorn
from pathlib import Path
from api import app, initialize_database_on_startup
from logging import basicConfig, DEBUG

def get_ssl_config():
    """SSL証明書の設定を取得"""
    
    # 環境変数から証明書パスを取得
    ssl_keyfile = os.getenv('SSL_KEYFILE')
    ssl_certfile = os.getenv('SSL_CERTFILE')
    
    # 開発環境: 自己署名証明書
    if not ssl_keyfile or not ssl_certfile:
        current_dir = Path(__file__).parent
        ssl_keyfile = current_dir / "server.key"
        ssl_certfile = current_dir / "server.crt"
        
        if not ssl_keyfile.exists() or not ssl_certfile.exists():
            print("❌ SSL証明書が見つかりません")
            print("   以下のいずれかを実行してください:")
            print("   1. 自己署名証明書の生成: python generate_ssl_cert.py")
            print("   2. Let's Encrypt証明書の設定: ./setup_letsencrypt.sh")
            print("   3. 環境変数の設定:")
            print("      export SSL_KEYFILE=/path/to/privkey.pem")
            print("      export SSL_CERTFILE=/path/to/fullchain.pem")
            return None, None
    
    return str(ssl_keyfile), str(ssl_certfile)

def create_ssl_context(ssl_keyfile: str, ssl_certfile: str):
    """SSL コンテキストを作成"""
    
    try:
        # SSL証明書の検証
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(ssl_certfile, ssl_keyfile)
        
        print("✅ SSL証明書を正常に読み込みました")
        print(f"   証明書: {ssl_certfile}")
        print(f"   秘密鍵: {ssl_keyfile}")
        
        return context
        
    except FileNotFoundError as e:
        print(f"❌ SSL証明書ファイルが見つかりません: {e}")
        return None
    except ssl.SSLError as e:
        print(f"❌ SSL証明書エラー: {e}")
        return None
    except Exception as e:
        print(f"❌ SSL設定エラー: {e}")
        return None

def main():
    """HTTPS サーバーを起動"""
    
    print("🔒 HTTPS APIサーバーを起動しています...")
    
    # SSL証明書の設定を取得
    ssl_keyfile, ssl_certfile = get_ssl_config()
    
    if not ssl_keyfile or not ssl_certfile:
        print("❌ SSL証明書の設定に失敗しました")
        return
    
    # SSL コンテキストを作成
    ssl_context = create_ssl_context(ssl_keyfile, ssl_certfile)
    
    if not ssl_context:
        print("❌ SSL コンテキストの作成に失敗しました")
        return
    
    # データベースの初期化
    print("📊 データベースを初期化中...")
    initialize_database_on_startup()
    
    # ログ設定
    basicConfig(level=DEBUG)
    
    # HTTPSサーバーの設定
    config = uvicorn.Config(
        app=app,
        host="0.0.0.0",
        port=8443,  # HTTPS用ポート
        ssl_keyfile=ssl_keyfile,
        ssl_certfile=ssl_certfile,
        log_level="info",
        access_log=True,
    )
    
    server = uvicorn.Server(config)
    
    print("🚀 HTTPSサーバーが起動しました!")
    print("   URL: https://localhost:8443")
    print("   URL: https://sakutai.net:8443")
    print("   ポート: 8443")
    print("   プロトコル: HTTPS")
    print()
    print("📋 接続テスト:")
    print("   curl -k https://localhost:8443/top/test/10")
    print()
    print("⚠️  注意事項:")
    print("   - 自己署名証明書の場合、ブラウザで警告が表示されます")
    print("   - 本番環境では信頼できるCAの証明書を使用してください")
    print("   - ファイアウォールでポート8443を開放してください")
    print()
    
    try:
        server.run()
    except KeyboardInterrupt:
        print("\n🛑 サーバーを停止しました")
    except Exception as e:
        print(f"❌ サーバーエラー: {e}")

if __name__ == "__main__":
    main()
