# -*- coding: cp1251 -*-
import logging
import sqlite3
from databases.KNS_11_1 import KNS_11_1_db
from databases.KNS_11_2 import KNS_11_2_db
from databases.KNS_12 import KNS_12_db
from databases.KNS_21_1 import KNS_21_1_db
from databases.KNS_21_2 import KNS_21_2_db


def get_all_schedule(group):
    group_set = eval(f'{group}_db')
    try:
        schedule_list = []
        group_set.cur.execute(f"SELECT * from {group}_mon")
        monday = group_set.cur.fetchall()
        group_set.cur.execute(f"SELECT * from {group}_tue")
        tuesday = group_set.cur.fetchall()
        group_set.cur.execute(f"SELECT * from {group}_wed")
        wednesday = group_set.cur.fetchall()
        group_set.cur.execute(f"SELECT * from {group}_thu")
        thursday = group_set.cur.fetchall()
        group_set.cur.execute(f"SELECT * from {group}_fri")
        friday = group_set.cur.fetchall()
        schedule_list.extend([monday, tuesday, wednesday, thursday, friday])

        return schedule_list
    except Exception as e:
        logging.error(e, exc_info=True)
        return 0
