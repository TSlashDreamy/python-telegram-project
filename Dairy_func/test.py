#-*- coding: cp1251 -*-
from pickle import FALSE
import pandas as pd
import sqlite3


con = sqlite3.connect("C:\\Users\\Max\\Desktop\\��\\���� ����� ��� ����\\DZ\\DZ_db.db")

cur = con.cursor()


#############  �������� ����� � �� ##################

# ��� �����
print("��� �����: ")
num = input()
name = input()
date = input()

# ��������� ����� � ������� (������� �� : ��������)

data ={'num':[num],
      'name':[name],
      'data':[date]}

#��������� ����� � ����-�����

df = pd.DataFrame(data)

# �������� ����-������ � ��

df.to_sql('DZ',con,if_exists='append', index = FALSE)
con.commit()

print("data frame")
print(df)
print("data base")
cur.execute('select * from DZ;')
print(cur.fetchall())

#############  ��������� ������ � �� ##################

delete_from_DB = "DELETE FROM DZ WHERE num = ?;"
num_delete = input()

# ��������� ����� �� ������� �� �����������

cur.execute(delete_from_DB, (num_delete,))
con.commit()

print("data base")
cur.execute('select * from DZ;')
print(cur.fetchall())

#############  ����������� ������  ##################

print("����������� �����: ")
num_update = input()
name_updated = str(input())
data_updated = str(input())
update_on_bd = "update DZ set name = ?, data = ? where num = ? "
cur.execute(update_on_bd, (name_updated, data_updated, num_update,))

print("data base")
cur.execute('select * from DZ;')
print(cur.fetchall())

con.close();