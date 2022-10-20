#-*- coding: cp1251 -*-
# import sqlite3 module
import sqlite3

if sqlite3.threadsafety == 3:
    check_same_thread = False
else:
    check_same_thread = True


con = sqlite3.connect("DZ_db.db", check_same_thread=check_same_thread)
  
# create the cursor object
cur = con.cursor()
  
# execute the script by creating the 
# table named geeks_demo and insert the data


######################    ПОНЕДІЛОК     ######################


cur.executescript("""
CREATE TABLE if not exists DZ (
   Num INT  PRIMARY KEY NOT NULL,
   UserId int NOT NULL,
   name char NOT NULL,
   data DATE NOT NULL
);""")



con.commit()
print(cur.fetchall())
con.close()