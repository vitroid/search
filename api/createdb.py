import sqlite3


def _createdb():
    con = sqlite3.connect("fav.db")

    cur = con.cursor()

    # Create tables
    cur.execute(
        """CREATE TABLE votes (id text PRIMARY KEY, favs text, timestamp text)"""
    )
    cur.execute(
        """CREATE TABLE favs (code text PRIMARY KEY, count integer DEFAULT 0)"""
    )

    # Save (commit) the changes
    con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    con.close()


if __name__ == "__main__":
    _createdb()
