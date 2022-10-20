import sqlite3
import time
from telebot.types import ReplyKeyboardRemove

from commands import diaryList
from core import botCore

global deleting_note
deleting_note = False

bot = botCore.bot
me = botCore.me
types = botCore.types


def delete_note(message):
    global deleting_note
    try:
        if deleting_note:
            note_to_delete = int(message.text)
    except Exception:
        bot.send_message(message.chat.id, "Некоректний ввід, введіть цифру без крапки:",
                         parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)
        return
    if deleting_note:
        con = sqlite3.connect("diary_notes/DZ_db.db", check_same_thread=False)
        cur = con.cursor()
        delete_from_DB = "DELETE FROM DZ WHERE num = ?;"
        cur.execute(delete_from_DB, (message.text,))
        con.commit()
        con.close()
        deleting_note = False
        bot.send_message(message.chat.id, f"✅ Записи з номером {message.text} видалено!",
                         parse_mode='html')
        diaryList.show_commands(message)
    elif not deleting_note:
        bot.send_message(message.chat.id, "✒ Напишіть цифру запису, який бажаєте видалити",
                         parse_mode='html', reply_markup=ReplyKeyboardRemove())
        bot.delete_message(message.chat.id, message.message_id)
        time.sleep(0.5)
        deleting_note = True
