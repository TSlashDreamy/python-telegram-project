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
con = sqlite3.connect("KNS_21_1_db.db",check_same_thread=check_same_thread)
  
# create the cursor object
cur = con.cursor()
  
# execute the script by creating the 
# table named geeks_demo and insert the data


######################    ����Ĳ���     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_1_mon (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_1_mon(NumPar, name,pochatokParu) VALUES(2,'����-��������� ������������� �����������','10:20')");
con.execute("INSERT or REPLACE INTO KNS_21_1_mon(NumPar, name,pochatokParu) VALUES(3,'������������� �������� ������ �����������' ,'12:10')");
con.execute("INSERT or REPLACE INTO KNS_21_1_mon(NumPar, name,pochatokParu) VALUES(4,'����-��������� ������������� ������','14:30')");
con.execute("INSERT or REPLACE INTO KNS_21_1_mon(NumPar, name,pochatokParu) VALUES(5,'����������� ���������� �������� ز �����������','16:20')");
con.commit()



######################    ²������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_1_tue (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_1_tue(NumPar, name,pochatokParu) VALUES(1,'_ /������������� �������� ������ ������ ','8:30')");
con.execute("INSERT or REPLACE INTO KNS_21_1_tue(NumPar, name,pochatokParu) VALUES(2,'������ �� ������ ���� ������/���� ������','10:20')");
con.commit()


######################    ������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_1_wed (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_1_wed(NumPar, name,pochatokParu) VALUES(1,'��������������� ����� ����� �����������','8:30')");
con.execute("INSERT or REPLACE INTO KNS_21_1_wed(NumPar, name,pochatokParu) VALUES(2,'���� �����������','10:20')");
con.commit()


######################    ������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_1_thu (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_1_thu(NumPar, name,pochatokParu) VALUES(1,'_ /��������������� ����� ����� ������','8:30')");
con.execute("INSERT or REPLACE INTO KNS_21_1_thu(NumPar, name,pochatokParu) VALUES(2,'������� �������� ������','10:20')");
con.execute("INSERT or REPLACE INTO KNS_21_1_thu(NumPar, name,pochatokParu) VALUES(3,'������� �������� �����������','12:10')");
con.execute("INSERT or REPLACE INTO KNS_21_1_thu(NumPar, name,pochatokParu) VALUES(4,'����� �������� ������ �����������','14:30')");
con.commit()



######################    �'������     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_1_fri (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_1_fri(NumPar, name,pochatokParu) VALUES(1,'_ /����������� ���������� �������� ز ������','8:20')");
con.execute("INSERT or REPLACE INTO KNS_21_1_fri(NumPar, name,pochatokParu) VALUES(2,'����� ��������� ������ ������/ _','10:20')");
con.execute("INSERT or REPLACE INTO KNS_21_1_fri(NumPar, name,pochatokParu) VALUES(3,'������ �� ������ ���� �����������','12:10')");

con.commit()


######################    ���� ���� �����     ######################



# display the data in the table by 
# executing the cursor object

print('################  ����Ĳ���  ################')
cur.execute("SELECT * from KNS_21_1_mon")
print(cur.fetchall())
'\n'
cur.execute("SELECT * from KNS_21_1_tue")
print('################  ²������  ################')
'\n'
print(cur.fetchall())
cur.execute("SELECT * from KNS_21_1_wed")
print('################  ������  ################')
'\n'
print(cur.fetchall())
cur.execute("SELECT * from KNS_21_1_thu")
print('################  ������  ################')
'\n'
print(cur.fetchall())
cur.execute("SELECT * from KNS_21_1_fri")
print('################  �������  ################')
print(cur.fetchall())




#cur.execute("SELECT group_id, name FROM groups WHERE WorkingDay = (SELECT strftime('%w',date()));");
  

