import sqlite3


def exec_sql(sql_code, params=None):
    conn = sqlite3.connect("test.db")
    try:
        cur = conn.cursor()
        if params:
            cur.execute(sql_code, params)
        else:
            cur.execute(sql_code)
        try:
            res = cur.fetchall()
        except Exception:
            res = []
        conn.commit()
        return res
    finally:
        conn.close()
