from core import botCore

bot = botCore.bot
me = botCore.me
types = botCore.types


def get_available_schedules(message):
    out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_button = types.KeyboardButton('КНС-11/1')
    second_button = types.KeyboardButton('КНС-11/2')
    third_button = types.KeyboardButton('КНС-12')
    fourth_button = types.KeyboardButton('КНС-21/1')
    fiveth_button = types.KeyboardButton('КНС-21/2')
    out_markup.add(first_button, second_button, third_button, fourth_button, fiveth_button)
    bot.send_message(message.chat.id, "Choose your group",
                     parse_mode='html', reply_markup=out_markup)
    bot.delete_message(message.chat.id, message.message_id)
