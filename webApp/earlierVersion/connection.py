#!/usr/bin/python3
"""This is a connection to db."""

import pymysql
dbconfig = {'host': 'localhost', 'user': 'vsearch', 'password': 'password',
            'db': 'vsearchlogdb'}
db = pymysql.connect(**dbconfig)
with db.cursor() as cursor:
    _sql = """show tables;"""

    cursor.execute(_sql)
    res = cursor.fetchall()
print(res)

with db.cursor() as cursor:
    _sql = """describe log;"""

    cursor.execute(_sql)
    res = cursor.fetchall()
for row in res:
    print(row)
