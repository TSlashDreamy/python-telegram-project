# -*- coding: cp1251 -*-
from pickle import FALSE
import pandas as pd
import sqlite3

global data


def database_input(number, note_name, note_date, user_id):
        global data
        con = sqlite3.connect("diary_notes/DZ_db.db", check_same_thread=False)
        cur = con.cursor()
        num = number
        name = note_name
        date = note_date
        user = user_id
        data = {'num': [num],
                'UserId': [user],
                'name': [name],
                'data': [date]}
        df = pd.DataFrame(data)
        df.to_sql('DZ', con, if_exists='append', index=FALSE)
        con.commit()
        con.close()

# print("data frame")
# print(df)
# print("data base")
# cur.execute('select * from DZ;')
# print(cur.fetchall())
#
# #############  ВИДАЛЕННЯ ЗАПИСУ З БД ##################
#
# delete_from_DB = "DELETE FROM DZ WHERE num = ?;"
# num_delete = input()
#
# # видалення рядка із номером від користувача
#
# cur.execute(delete_from_DB, (num_delete,))
# con.commit()
