import sqlite3
import time
from telebot.types import ReplyKeyboardRemove

from commands import diaryList
from core import botCore
from diary_notes import getDiaryData

global deleting_note, request_from_user, validity
deleting_note = False
validity = True
request_from_user = 0

bot = botCore.bot
me = botCore.me
types = botCore.types


def check_database(message):
    global validity
    if request_from_user != 0 and request_from_user == message.from_user.id:
        try:
            data = getDiaryData.get_data()
            number = int(message.text.split(".", 1)[0])
            content = message.text.split(".", 1)[1]
            validity = False
            for i in range(len(data)):
                i += 1
                if data[i][1] == message.from_user.id:
                    if data[i][0] == number and data[i][2] == content:
                        validity = True
                        break
            if not validity:
                bot.send_message(message.chat.id, "❌ У Вас немає такого запису",
                                 parse_mode='html')
                bot.delete_message(message.chat.id, message.id)
                return
        except Exception:
            bot.send_message(message.chat.id, "❌ У Вас немає такого запису",
                             parse_mode='html')
            bot.delete_message(message.chat.id, message.id)



def delete_note(message):
    global deleting_note, request_from_user, validity
    check_database(message)
    if not validity:
        return
    if deleting_note and request_from_user == message.from_user.id:
        print("deleting")
        con = sqlite3.connect("diary_notes/DZ_db.db", check_same_thread=False)
        cur = con.cursor()
        number = message.text.split(".", 1)[0]
        content = message.text.split(".", 1)[1]
        delete_from_DB = "DELETE FROM DZ WHERE num = ? AND name = ? AND UserId = ?;"
        cur.execute(delete_from_DB, (number, content, message.from_user.id,))
        con.commit()
        con.close()
        deleting_note = False
        request_from_user = 0
        bot_message = bot.send_message(message.chat.id, f"✅ Запис №{number} видалено!",
                         parse_mode='html')
        bot.delete_message(message.chat.id, bot_message.id - 2)
        bot.delete_message(message.chat.id, message.id)
        diaryList.show_commands(message, "call")
    elif not deleting_note and request_from_user == 0:
        out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        data = getDiaryData.get_data()
        print("entered delete mode")
        request_from_user = message.from_user.id
        if data != 0:
            for i in range(len(data)):
                if data[i][1] == message.from_user.id:
                    out_markup.add(types.KeyboardButton(f'{data[i][0]}.{data[i][2]}'))
            bot_message = bot.send_message(message.chat.id, "Оберіть запис, який бажаєте видалити за допомогою кнопки",
                             parse_mode='html', reply_markup=out_markup)
            bot.delete_message(message.chat.id, message.id)
            bot.delete_message(message.chat.id, bot_message.id - 2)
        else:
            bot.send_message(message.chat.id, "📂 У Вас немає записів для видалення",
                             parse_mode='html')
        # safe sleep
        time.sleep(0.2)
        deleting_note = True
    elif request_from_user != message.from_user.id:
        print("informing user")
        bot.send_message(message.chat.id, "⚠️О ні!\nНа даний момент це не доступно :с\nПовторіть спробу через декілька "
                                          "секунд ",
                         parse_mode='html')
        bot.delete_message(message.chat.id, message.id)
