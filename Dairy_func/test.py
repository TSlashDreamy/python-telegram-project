#-*- coding: cp1251 -*-
from pickle import FALSE
import pandas as pd
import sqlite3


con = sqlite3.connect("C:\\Users\\Max\\Desktop\\ДЗ\\Бази Даних для бота\\DZ\\DZ_db.db")

cur = con.cursor()


#############  ВНЕСЕННЯ ДАНИХ У БД ##################

# ввід даних
print("Ввід даних: ")
num = input()
name = input()
date = input()

# занесення даних у словник (колонка БД : значення)

data ={'num':[num],
      'name':[name],
      'data':[date]}

#занесення даних у дата-фрейм

df = pd.DataFrame(data)

# Внесення дата-фрейму у бд

df.to_sql('DZ',con,if_exists='append', index = FALSE)
con.commit()

print("data frame")
print(df)
print("data base")
cur.execute('select * from DZ;')
print(cur.fetchall())

#############  ВИДАЛЕННЯ ЗАПИСУ З БД ##################

delete_from_DB = "DELETE FROM DZ WHERE num = ?;"
num_delete = input()

# видалення рядка із номером від користувача

cur.execute(delete_from_DB, (num_delete,))
con.commit()

print("data base")
cur.execute('select * from DZ;')
print(cur.fetchall())

#############  РЕДАГУВАННЯ ЗАПИСУ  ##################

print("Редагування даних: ")
num_update = input()
name_updated = str(input())
data_updated = str(input())
update_on_bd = "update DZ set name = ?, data = ? where num = ? "
cur.execute(update_on_bd, (name_updated, data_updated, num_update,))

print("data base")
cur.execute('select * from DZ;')
print(cur.fetchall())

con.close();