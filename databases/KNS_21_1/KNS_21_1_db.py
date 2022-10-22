#-*- coding: cp1251 -*-
# import sqlite3 module
import sqlite3

con = sqlite3.connect("databases/KNS_21_1/KNS_21_1_db.db", check_same_thread=False)
  
# create the cursor object
cur = con.cursor()


######################    ПОНЕДІЛОК     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_1_mon (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_1_mon(NumPar, name,pochatokParu) VALUES(2,'Крос-платфомне програмування лабораторна','10:20')");
con.execute("INSERT or REPLACE INTO KNS_21_1_mon(NumPar, name,pochatokParu) VALUES(3,'Програмування мобільних систем лабораторна' ,'12:10')");
con.execute("INSERT or REPLACE INTO KNS_21_1_mon(NumPar, name,pochatokParu) VALUES(4,'Крос-платфомне програмування лекція','14:30')");
con.execute("INSERT or REPLACE INTO KNS_21_1_mon(NumPar, name,pochatokParu) VALUES(5,'Опрацювання інформації методами ШІ лабораторна','16:20')");
con.commit()



######################    ВІВТОРОК     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_1_tue (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_1_tue(NumPar, name,pochatokParu) VALUES(1,'_ /Програмування мобільних систем лекція ','8:30')");
con.execute("INSERT or REPLACE INTO KNS_21_1_tue(NumPar, name,pochatokParu) VALUES(2,'Методи та засоби ООАП лекція/ТРПО лекція','10:20')");
con.commit()


######################    СЕРЕДА     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_1_wed (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_1_wed(NumPar, name,pochatokParu) VALUES(1,'Інтелектуальний аналіз даних лабораторна','8:30')");
con.execute("INSERT or REPLACE INTO KNS_21_1_wed(NumPar, name,pochatokParu) VALUES(2,'ТРПО лабораторна','10:20')");
con.commit()


######################    ЧЕТВЕР     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_1_thu (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_1_thu(NumPar, name,pochatokParu) VALUES(1,'_ /Інтелектуальний аналіз даних лекція','8:30')");
con.execute("INSERT or REPLACE INTO KNS_21_1_thu(NumPar, name,pochatokParu) VALUES(2,'Машинне навчання лекція','10:20')");
con.execute("INSERT or REPLACE INTO KNS_21_1_thu(NumPar, name,pochatokParu) VALUES(3,'Машинне навчання лабораторна','12:10')");
con.execute("INSERT or REPLACE INTO KNS_21_1_thu(NumPar, name,pochatokParu) VALUES(4,'Теорія прийнття рішення лабораторна','14:30')");
con.commit()



######################    П'ЯТНИЦЯ     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_21_1_fri (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_21_1_fri(NumPar, name,pochatokParu) VALUES(1,'_ /Опрацювання інформації методами ШІ лекція','8:20')");
con.execute("INSERT or REPLACE INTO KNS_21_1_fri(NumPar, name,pochatokParu) VALUES(2,'Теорія прийняття рішення лекція/ _','10:20')");
con.execute("INSERT or REPLACE INTO KNS_21_1_fri(NumPar, name,pochatokParu) VALUES(3,'Методи та засоби ООАП лабораторна','12:10')");

con.commit()
