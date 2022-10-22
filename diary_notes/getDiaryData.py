#-*- coding: cp1251 -*-
import sqlite3


# cur.executescript("""
# CREATE TABLE if not exists DZ (
#    Num INT  PRIMARY KEY NOT NULL,
#    UserId int NOT NULL,
#    name char NOT NULL,
#    data DATE NOT NULL
# );""")


def get_data():
    try:
        con = sqlite3.connect("diary_notes/DZ_db.db", check_same_thread=False)
        cur = con.cursor()
        cur.execute('select * From DZ')
        data = cur.fetchall()
        con.close()
        if not data:
            return 0
        return data
    except:
        return 0


# con.commit()
# print(cur.fetchall())

