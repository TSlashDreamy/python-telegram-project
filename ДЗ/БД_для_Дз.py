#-*- coding: cp1251 -*-
# import sqlite3 module
import sqlite3
# create con object to connect 
# the database geeks_db.db
con = sqlite3.connect("DZ_db.db")
  
# create the cursor object
cur = con.cursor()
  
# execute the script by creating the 
# table named geeks_demo and insert the data


######################    ПОНЕДІЛОК     ######################


cur.executescript("""
CREATE TABLE if not exists DZ (
   Num INT  PRIMARY KEY NOT NULL,
   name char NOT NULL,
   data DATE NOT NULL
);""")



con.commit()
print(cur.fetchall())
con.close()