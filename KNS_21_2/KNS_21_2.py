#-*- coding: cp1251 -*-
# import sqlite3 module
import sqlite3
from datetime import datetime
# create con object to connect 
# the database geeks_db.db
if sqlite3.threadsafety == 3:
    check_same_thread = False
else:
    check_same_thread = True
con = sqlite3.connect("KNS_21_2_db.db",check_same_thread=check_same_thread)
  
# create the cursor object
cur = con.cursor()
  
# execute the script by creating the 
# table named geeks_demo and insert the data


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


######################    ���� ���� �����     ######################



# display the data in the table by 
# executing the cursor object

print('################  ����Ĳ���  ################')
cur.execute("SELECT * from KNS_21_2_mon")
print(cur.fetchall())
'\n'
cur.execute("SELECT * from KNS_21_2_tue")
print('################  ²������  ################')
'\n'
print(cur.fetchall())
cur.execute("SELECT * from KNS_21_2_wed")
print('################  ������  ################')
'\n'
print(cur.fetchall())
cur.execute("SELECT * from KNS_21_2_thu")
print('################  ������  ################')
'\n'
print(cur.fetchall())
cur.execute("SELECT * from KNS_21_2_fri")
print('################  �������  ################')
print(cur.fetchall())




#cur.execute("SELECT group_id, name FROM groups WHERE WorkingDay = (SELECT strftime('%w',date()));");
  

