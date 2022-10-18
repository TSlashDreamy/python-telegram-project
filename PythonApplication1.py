# -*- coding: cp1251 -*-
# import sqlite3 module
import sqlite3
from datetime import datetime

# if sqlite3.threadsafety == 3:
#     check_same_thread = False
# else:
#     check_same_thread = True

con = sqlite3.connect("KNS_11_2_db.db", check_same_thread=False)

# create the cursor object
cur = con.cursor()

# execute the script by creating the
# table named geeks_demo and insert the data


######################    ����Ĳ���     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_11_2_mon (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute(
    "INSERT or REPLACE INTO KNS_11_2_mon(NumPar, name,pochatokParu) VALUES(2,'��������� ����� �����������','10:20')");
con.execute("INSERT or REPLACE INTO KNS_11_2_mon(NumPar, name,pochatokParu) VALUES(3,'��� �����������','12:10')");
con.commit()

######################    ²������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_11_2_tue (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute(
    "INSERT or REPLACE INTO KNS_11_2_tue(NumPar, name,pochatokParu) VALUES(1,'����������� ������ �����������','8:30')");
con.execute(
    "INSERT or REPLACE INTO KNS_11_2_tue(NumPar, name,pochatokParu) VALUES(2,'������� �������� ��������� �����������','10:20')");
con.execute(
    "INSERT or REPLACE INTO KNS_11_2_tue(NumPar, name,pochatokParu) VALUES(3,'����������� ������ ������','12:10')");
con.execute(
    "INSERT or REPLACE INTO KNS_11_2_tue(NumPar, name,pochatokParu) VALUES(4,'����������� ��� ������ ����� ����� Pyton ������','14:30')");
con.commit()

######################    ������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_11_2_wed (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute(
    "INSERT or REPLACE INTO KNS_11_2_wed(NumPar, name,pochatokParu) VALUES(2,'���������� ��� ����� �� ����� �����������','10:20')");
con.execute(
    "INSERT or REPLACE INTO KNS_11_2_wed(NumPar, name,pochatokParu) VALUES(3,'���������� ��� ����� �� ����� ������ / ��������� ��-��������� ������', '12:10')");
con.execute(
    "INSERT or REPLACE INTO KNS_11_2_wed(NumPar, name,pochatokParu) VALUES(4,'������� �������� ��������� ������ / ������������ ���������������� ','14:30')");
con.execute(
    "INSERT or REPLACE INTO KNS_11_2_wed(NumPar, name,pochatokParu) VALUES(5,'���������� ��� ����� �� ����� ����������� / _','16:10')");
con.commit()

######################    ������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_11_2_thu (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute(
    "INSERT or REPLACE INTO KNS_11_2_thu(NumPar, name,pochatokParu) VALUES(1,'������������� ��� ������ ����� ����� Pyton �����������','8:30')");
con.execute(
    "INSERT or REPLACE INTO KNS_11_2_thu(NumPar, name,pochatokParu) VALUES(2,'��������� ��-��������� �����������','10:20')");
con.execute(
    "INSERT or REPLACE INTO KNS_11_2_thu(NumPar, name,pochatokParu) VALUES(3,'��������� ����� ������','12:10')");
con.execute("INSERT or REPLACE INTO KNS_11_2_thu(NumPar, name,pochatokParu) VALUES(4,'��� ������','14:30')");
con.commit()

######################    �'������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_11_2_fri (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute(
    "INSERT or REPLACE INTO KNS_11_2_fri(NumPar, name,pochatokParu) VALUES(2,'�������� � ����� ������','10:20')");
con.execute(
    "INSERT or REPLACE INTO KNS_11_2_fri(NumPar, name,pochatokParu) VALUES(3,'�������� � ����� �������� / _','12:10')");
con.commit()


def get_all_schedule(group):
    try:
        schedule_list = []
        cur.execute(f"SELECT * from {group}_mon")
        monday = cur.fetchall()
        cur.execute(f"SELECT * from {group}_tue")
        tuesday = cur.fetchall()
        cur.execute(f"SELECT * from {group}_wed")
        wednesday = cur.fetchall()
        cur.execute(f"SELECT * from {group}_thu")
        thursday = cur.fetchall()
        cur.execute(f"SELECT * from {group}_fri")
        friday = cur.fetchall()
        schedule_list.extend([monday, tuesday, wednesday, thursday, friday])

        return schedule_list
    except:
        return 0
