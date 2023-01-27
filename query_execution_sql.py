import sqlite3


query_file = 'query_3.sql'

with open(f"queryes/{query_file}", 'r') as query:
    sql = query.read()


def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


print(execute_query(sql))
