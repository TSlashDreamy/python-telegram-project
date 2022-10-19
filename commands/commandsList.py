from core import botCore

bot = botCore.bot
me = botCore.me
types = botCore.types


def show_commands(message):
    out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    schedule_button = types.KeyboardButton('📃 Розклад')
    date_button = types.KeyboardButton('📅 Точна дата')
    out_markup.add(schedule_button, date_button)
    bot.send_message(message.chat.id, "Оберіть бажану команду однією з кнопок нижче",
                     parse_mode='html', reply_markup=out_markup)
    bot.delete_message(message.chat.id, message.message_id)
