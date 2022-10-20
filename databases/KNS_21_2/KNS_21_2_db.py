#-*- coding: cp1251 -*-
import sqlite3

con = sqlite3.connect("databases/KNS_21_2/KNS_21_2_db.db", check_same_thread=False)
  
# create the cursor object
cur = con.cursor()


######################    ����Ĳ���     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_2_mon (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_2_mon(NumPar, name,pochatokParu) VALUES(4,'����-��������� ������������� ������','14:30')");
con.execute("INSERT or REPLACE INTO KNS_21_2_mon(NumPar, name,pochatokParu) VALUES(5,'��������������� ����� ����� �����������','16:20')");
con.commit()



######################    ²������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_2_tue (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_2_tue(NumPar, name,pochatokParu) VALUES(1,'_ /������������� �������� ������ ������ ','8:30')");
con.execute("INSERT or REPLACE INTO KNS_21_2_tue(NumPar, name,pochatokParu) VALUES(2,'������ �� ������ ���� ������/���� ������','10:20')");
con.commit()


######################    ������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_2_wed (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_2_wed(NumPar, name,pochatokParu) VALUES(1,'����������� ���������� �������� ز �����������','8:30')");
con.execute("INSERT or REPLACE INTO KNS_21_2_wed(NumPar, name,pochatokParu) VALUES(2,'������� �������� �����������','10:20')");
con.execute("INSERT or REPLACE INTO KNS_21_2_wed(NumPar, name,pochatokParu) VALUES(3,'���� �����������','12:10')");
con.execute("INSERT or REPLACE INTO KNS_21_2_wed(NumPar, name,pochatokParu) VALUES(4,'������ �� ������ ���� �����������','14:30')");
con.commit()


######################    ������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_2_thu (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_2_thu(NumPar, name,pochatokParu) VALUES(1,'_ /��������������� ����� ����� ������','8:30')");
con.execute("INSERT or REPLACE INTO KNS_21_2_thu(NumPar, name,pochatokParu) VALUES(2,'������� �������� ������','10:20')");
con.execute("INSERT or REPLACE INTO KNS_21_2_thu(NumPar, name,pochatokParu) VALUES(3,'����-��������� ������������� �����������','12:10')");
con.execute("INSERT or REPLACE INTO KNS_21_2_thu(NumPar, name,pochatokParu) VALUES(4,'������������� �������� ������ �����������','14:30')");
con.commit()



######################    �'������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_2_fri (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_2_fri(NumPar, name,pochatokParu) VALUES(1,'_ /����������� ���������� �������� ز ������','8:20')");
con.execute("INSERT or REPLACE INTO KNS_21_2_fri(NumPar, name,pochatokParu) VALUES(2,'����� ��������� ������ ������/ _','10:20')");
con.execute("INSERT or REPLACE INTO KNS_21_2_fri(NumPar, name,pochatokParu) VALUES(3,'����� ��������� ������ ������ �����������','12:10')");
con.commit()