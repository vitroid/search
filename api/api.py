# from logging import getLogger, DEBUG, basicConfig
import hashlib
import json
import sqlite3
import time
from collections import defaultdict
from logging import getLogger
import re
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

con = sqlite3.connect("fav.db")
# hardcoded

app = FastAPI()

# basicConfig(level=DEBUG)   # add this line

origins = [
    "*",
    "http://153.120.1.15",
    "http://www.chem.okayama-u.ac.jp",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

    ids = []
    for id, favs in cur.execute(
        "SELECT id, favs FROM votes WHERE timestamp < :expiry",
        {"expiry": expiry},
    ):
        logger.info(f"expire: {id}")
        ids.append(id)
        yield to_dict(favs)
    cur.execute("DELETE FROM votes WHERE id IN (:ids)", {"ids": ",".join(ids)})


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

    logger.info("0")
    if not valid(v.id):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid ID",
            headers={"WWW-Authenticate": "Basic"},
        )

    # DB
    cur = con.cursor()

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

    con.commit()


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

    # DB
    cur = con.cursor()

    return json.dumps(
        dict(
            cur.execute(
                "SELECT code, count FROM favs ORDER BY count DESC LIMIT :num",
                {"num": num},
            )
        )
    )
    # /DB


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8090,
    )
