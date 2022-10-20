import time
from telebot.types import ReplyKeyboardRemove
from core import botCore

global inputting_note
inputting_note = False


types = botCore.types
bot = botCore.bot
me = botCore.me


def trigger_event(message):
    global inputting_note
    bot.send_message(message.chat.id, "✒ Введіть Ваш запис: ",
                     parse_mode='html', reply_markup=ReplyKeyboardRemove())
    bot.delete_message(message.chat.id, message.message_id)
    time.sleep(0.5)
    inputting_note = True
