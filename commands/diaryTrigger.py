import time
from telebot.types import ReplyKeyboardRemove
from core import botCore

global inputting_note, input_for_user
inputting_note = False
input_for_user = 0


types = botCore.types
bot = botCore.bot
me = botCore.me


def trigger_event(message):
    global inputting_note, input_for_user
    if input_for_user == 0:
        input_for_user = message.from_user.id
        bot_message = bot.send_message(message.chat.id, "✒ Введіть Ваш запис: ",
                         parse_mode='html', reply_markup=ReplyKeyboardRemove())
        bot.delete_message(message.chat.id, message.id)
        bot.delete_message(message.chat.id, bot_message.id - 2)
        # safe sleep
        time.sleep(0.2)
        inputting_note = True
    else:
        bot.send_message(message.chat.id, "⚠️О ні!\nНа даний момент це не доступно :с\nПовторіть спробу через декілька "
                                          "секунд ",
                         parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)
