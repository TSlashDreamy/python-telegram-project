#-*- coding: cp1251 -*-
# import sqlite3 module
import sqlite3
from datetime import datetime
# create con object to connect 
# the database geeks_db.db
con = sqlite3.connect("KNS_11_2_db.db")
  
# create the cursor object
cur = con.cursor()
  
# execute the script by creating the 
# table named geeks_demo and insert the data


######################    ПОНЕДІЛОК     ######################


cur.executescript("""
CREATE TABLE if not exists KN_11_2_mon (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KN_11_2_mon(NumPar, name,pochatokParu) VALUES(2,'Компютерні мережі лабораторна','10:20')");
con.execute("INSERT or REPLACE INTO KN_11_2_mon(NumPar, name,pochatokParu) VALUES(3,'ООП лабораторна','12:10')");
con.commit()


######################    ВІВТОРОК     ######################


cur.executescript("""
CREATE TABLE if not exists KN_11_2_tue (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KN_11_2_tue(NumPar, name,pochatokParu) VALUES(1,'Моделювання систем лабораторна','8:30')");
con.execute("INSERT or REPLACE INTO KN_11_2_tue(NumPar, name,pochatokParu) VALUES(2,'Системи штучного інтелекту лабораторна','10:20')");
con.execute("INSERT or REPLACE INTO KN_11_2_tue(NumPar, name,pochatokParu) VALUES(3,'Моделювання систем лекція','12:10')");
con.execute("INSERT or REPLACE INTO KN_11_2_tue(NumPar, name,pochatokParu) VALUES(4,'Прогмування для аналізу даних мовою Pyton лекція','14:30')");
con.commit()


######################    СЕРЕДА     ######################


cur.executescript("""
CREATE TABLE if not exists KN_11_2_wed (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KN_11_2_wed(NumPar, name,pochatokParu) VALUES(2,'Організація баз даних та знань лабораторна','10:20')");
con.execute("INSERT or REPLACE INTO KN_11_2_wed(NumPar, name,pochatokParu) VALUES(3,'Організація баз даних та знань лекція / Управління ІТ-проектами лекція', '12:10')");
con.execute("INSERT or REPLACE INTO KN_11_2_wed(NumPar, name,pochatokParu) VALUES(4,'Системи штучного інтелекту лекція / Адаптаційний курсадаптаційний ','14:30')");
con.execute("INSERT or REPLACE INTO KN_11_2_wed(NumPar, name,pochatokParu) VALUES(5,'Організація баз даних та знань лабораторна / _','16:10')");
con.commit()


######################    ЧЕТВЕР     ######################


cur.executescript("""
CREATE TABLE if not exists KN_11_2_thu (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KN_11_2_thu(NumPar, name,pochatokParu) VALUES(1,'Програмування для аналізу даних мовою Pyton лабораторна','8:30')");
con.execute("INSERT or REPLACE INTO KN_11_2_thu(NumPar, name,pochatokParu) VALUES(2,'Управління ІТ-проектами лабораторна','10:20')");
con.execute("INSERT or REPLACE INTO KN_11_2_thu(NumPar, name,pochatokParu) VALUES(3,'Компютерні мережі лекція','12:10')");
con.execute("INSERT or REPLACE INTO KN_11_2_thu(NumPar, name,pochatokParu) VALUES(4,'ООП лекція','14:30')");
con.commit()


######################    П'ЯТНИЦЯ     ######################


cur.executescript("""
CREATE TABLE if not exists KN_11_2_fri (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KN_11_2_fri(NumPar, name,pochatokParu) VALUES(2,'Економіка і бізнес лекція','10:20')");
con.execute("INSERT or REPLACE INTO KN_11_2_fri(NumPar, name,pochatokParu) VALUES(3,'Економіка і бізнес практичні / _','12:10')");
con.commit()


######################    ТЕСТ БАЗИ ДАНИХ     ######################



# display the data in the table by 
# executing the cursor object
print('################  ПОНЕДІЛОК  ################')
cur.execute("SELECT * from KN_11_2_mon")
print(cur.fetchall())
'\n'
cur.execute("SELECT * from KN_11_2_tue")
print('################  ВІВТОРОК  ################')
'\n'
print(cur.fetchall())
cur.execute("SELECT * from KN_11_2_wed")
print('################  СЕРЕДА  ################')
'\n'
print(cur.fetchall())
cur.execute("SELECT * from KN_11_2_thu")
print('################  ЧЕТВЕР  ################')
'\n'
print(cur.fetchall())
cur.execute("SELECT * from KN_11_2_fri")
print('################  ПЯТНИЦЯ  ################')
print(cur.fetchall())



#cur.execute("SELECT group_id, name FROM groups WHERE WorkingDay = (SELECT strftime('%w',date()));");
  
