# -*- coding: cp1251 -*-
import sqlite3

con = sqlite3.connect("databases/KNS_12/KNS_12_db.db", check_same_thread=False)

# create the cursor object
cur = con.cursor()


######################    ����Ĳ���     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_12_mon (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute(
    "INSERT or REPLACE INTO KNS_12_mon(NumPar, name,pochatokParu) VALUES(2,'���������� ��� ����� �����������','10:20')");
con.execute(
    "INSERT or REPLACE INTO KNS_12_mon(NumPar, name,pochatokParu) VALUES(3,'_ /���������� ��� ����� �����������' ,'12:10')");
con.execute("INSERT or REPLACE INTO KNS_12_mon(NumPar, name,pochatokParu) VALUES(4,'��� �����������','14:30')");
con.execute(
    "INSERT or REPLACE INTO KNS_12_mon(NumPar, name,pochatokParu) VALUES(5,'����������� ������ �����������','16:20')");
con.commit()

######################    ²������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_12_tue (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute(
    "INSERT or REPLACE INTO KNS_12_tue(NumPar, name,pochatokParu) VALUES(1,'������� �������� ��������� ','8:30')");
con.execute(
    "INSERT or REPLACE INTO KNS_12_tue(NumPar, name,pochatokParu) VALUES(2,'��������� ����� ����������� ','10:20')");
con.commit()

######################    ������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_12_wed (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute(
    "INSERT or REPLACE INTO KNS_12_wed(NumPar, name,pochatokParu) VALUES(2,'������������� ��� ������ ����� ����� Pyton �����������','12:10')");
con.execute(
    "INSERT or REPLACE INTO KNS_12_wed(NumPar, name,pochatokParu) VALUES(3,'��������� ��-��������� �����������','14:30')");
con.execute(
    "INSERT or REPLACE INTO KNS_12_wed(NumPar, name,pochatokParu) VALUES(4,'���������� ��� ����� �� ����� �����������','16:20')");
con.commit()

######################    ������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_12_thu (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute(
    "INSERT or REPLACE INTO KNS_12_thu(NumPar, name,pochatokParu) VALUES(3,'��������� ����� ������','12:10')");
con.execute("INSERT or REPLACE INTO KNS_12_thu(NumPar, name,pochatokParu) VALUES(4,'��� ������','14:30')");
con.commit()

######################    �'������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_12_fri (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute(
    "INSERT or REPLACE INTO KNS_12_fri(NumPar, name,pochatokParu) VALUES(2,'�������� � ����� ������','10:20')");
con.execute(
    "INSERT or REPLACE INTO KNS_12_fri(NumPar, name,pochatokParu) VALUES(3,'�������� � ����� ��������','12:10')");
con.commit()
