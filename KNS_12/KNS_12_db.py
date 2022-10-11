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
con = sqlite3.connect("KNS_12_db.db",check_same_thread=check_same_thread)
  
# create the cursor object
cur = con.cursor()
  
# execute the script by creating the 
# table named geeks_demo and insert the data


######################    ПОНЕДІЛОК     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_12_mon (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_12_mon(NumPar, name,pochatokParu) VALUES(2,'Організація баз даних лабораторна','10:20')");
con.execute("INSERT or REPLACE INTO KNS_12_mon(NumPar, name,pochatokParu) VALUES(3,'_ /Організація баз даних лабораторна' ,'12:10')");
con.execute("INSERT or REPLACE INTO KNS_12_mon(NumPar, name,pochatokParu) VALUES(4,'ООП лабораторна','14:30')");
con.execute("INSERT or REPLACE INTO KNS_12_mon(NumPar, name,pochatokParu) VALUES(5,'Моделювання систем лабораторна','16:20')");
con.commit()



######################    ВІВТОРОК     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_12_tue (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_12_tue(NumPar, name,pochatokParu) VALUES(1,'Системи штучного інтелекту ','8:30')");
con.execute("INSERT or REPLACE INTO KNS_12_tue(NumPar, name,pochatokParu) VALUES(2,'Компютерні мережі лабораторна ','10:20')");
con.commit()


######################    СЕРЕДА     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_12_wed (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_12_wed(NumPar, name,pochatokParu) VALUES(2,'Програмування для аналізу даних мовою Pyton лабораторна','12:10')");
con.execute("INSERT or REPLACE INTO KNS_12_wed(NumPar, name,pochatokParu) VALUES(3,'Управління ІТ-проектами лабораторна','14:30')");
con.execute("INSERT or REPLACE INTO KNS_12_wed(NumPar, name,pochatokParu) VALUES(4,'Організація баз даних та знань лабораторна','16:20')");
con.commit()


######################    ЧЕТВЕР     ######################


cur.executescript("""
CREATE TABLE if not exists KNS_12_thu (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KNS_12_thu(NumPar, name,pochatokParu) VALUES(3,'Компютерні мережі лекція','12:10')");
con.execute("INSERT or REPLACE INTO KNS_12_thu(NumPar, name,pochatokParu) VALUES(4,'ООП лекція','14:30')");
con.commit()



######################    П'ЯТНИЦЯ     ######################


cur.executescript("""
CREATE TABLE if not exists KN_11_1_fri (
   NumPar INT  PRIMARY KEY NOT NULL,
   name TEXT NOT NULL,
   pochatokParu TIME NOT NULL
);""")

con.execute("INSERT or REPLACE INTO KN_11_1_fri(NumPar, name,pochatokParu) VALUES(2,'Економіка і бізнес лекція','10:20')");
con.execute("INSERT or REPLACE INTO KN_11_1_fri(NumPar, name,pochatokParu) VALUES(3,'Економіка і бізнес практичні','12:10')");
con.commit()


######################    ТЕСТ БАЗИ ДАНИХ     ######################



# display the data in the table by 
# executing the cursor object

print('################  ПОНЕДІЛОК  ################')
cur.execute("SELECT * from KNS_12_mon")
print(cur.fetchall())
'\n'
cur.execute("SELECT * from KNS_12_tue")
print('################  ВІВТОРОК  ################')
'\n'
print(cur.fetchall())
cur.execute("SELECT * from KNS_12_wed")
print('################  СЕРЕДА  ################')
'\n'
print(cur.fetchall())
cur.execute("SELECT * from KNS_12_thu")
print('################  ЧЕТВЕР  ################')
'\n'
print(cur.fetchall())
cur.execute("SELECT * from KN_11_1_fri")
print('################  ПЯТНИЦЯ  ################')
print(cur.fetchall())




#cur.execute("SELECT group_id, name FROM groups WHERE WorkingDay = (SELECT strftime('%w',date()));");
  
