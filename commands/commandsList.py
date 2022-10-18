from core import botCore

bot = botCore.bot
me = botCore.me
types = botCore.types


def show_commands(message):
    out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    shedule_button = types.KeyboardButton('📃 Schedules')
    date_button = types.KeyboardButton('📅 Check date status')
    out_markup.add(shedule_button, date_button)
    bot.send_message(message.chat.id, "Choose what you want by pressing a button",
                     parse_mode='html', reply_markup=out_markup)
    bot.delete_message(message.chat.id, message.message_id)
