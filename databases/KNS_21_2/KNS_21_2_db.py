#-*- coding: cp1251 -*-
import sqlite3

con = sqlite3.connect("databases/KNS_21_2/KNS_21_2_db.db", check_same_thread=False)
  
# create the cursor object
cur = con.cursor()


######################    ПОНЕДІЛОК     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_2_mon (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_2_mon(NumPar, name,pochatokParu) VALUES(4,'Крос-платфомне програмування лекція','14:30')");
con.execute("INSERT or REPLACE INTO KNS_21_2_mon(NumPar, name,pochatokParu) VALUES(5,'Інтелектуальний аналіз даних лабораторна','16:20')");
con.commit()



######################    ВІВТОРОК     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_2_tue (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_2_tue(NumPar, name,pochatokParu) VALUES(1,'_ /Програмування мобільних систем лекція ','8:30')");
con.execute("INSERT or REPLACE INTO KNS_21_2_tue(NumPar, name,pochatokParu) VALUES(2,'Методи та засоби ООАП лекція/ТРПО лекція','10:20')");
con.commit()


######################    СЕРЕДА     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_2_wed (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_2_wed(NumPar, name,pochatokParu) VALUES(1,'Опрацювання інформації методами ШІ лабораторна','8:30')");
con.execute("INSERT or REPLACE INTO KNS_21_2_wed(NumPar, name,pochatokParu) VALUES(2,'Машинне навчання лабораторна','10:20')");
con.execute("INSERT or REPLACE INTO KNS_21_2_wed(NumPar, name,pochatokParu) VALUES(3,'ТРПО лабораторна','12:10')");
con.execute("INSERT or REPLACE INTO KNS_21_2_wed(NumPar, name,pochatokParu) VALUES(4,'Методи та засоби ООАП лабораторна','14:30')");
con.commit()


######################    ЧЕТВЕР     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_2_thu (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_2_thu(NumPar, name,pochatokParu) VALUES(1,'_ /Інтелектуальний аналіз даних лекція','8:30')");
con.execute("INSERT or REPLACE INTO KNS_21_2_thu(NumPar, name,pochatokParu) VALUES(2,'Машинне навчання лекція','10:20')");
con.execute("INSERT or REPLACE INTO KNS_21_2_thu(NumPar, name,pochatokParu) VALUES(3,'Крос-платфомне програмування лабораторна','12:10')");
con.execute("INSERT or REPLACE INTO KNS_21_2_thu(NumPar, name,pochatokParu) VALUES(4,'Програмування мобільних систем лабораторна','14:30')");
con.commit()



######################    П'ЯТНИЦЯ     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_2_fri (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_2_fri(NumPar, name,pochatokParu) VALUES(1,'_ /Опрацювання інформації методами ШІ лекція','8:20')");
con.execute("INSERT or REPLACE INTO KNS_21_2_fri(NumPar, name,pochatokParu) VALUES(2,'Теорія прийняття рішення лекція/ _','10:20')");
con.execute("INSERT or REPLACE INTO KNS_21_2_fri(NumPar, name,pochatokParu) VALUES(3,'Теорія прийняття рішення лекція лабораторна','12:10')");
con.commit()
