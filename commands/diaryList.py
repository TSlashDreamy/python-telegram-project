from core import botCore

bot = botCore.bot
me = botCore.me
types = botCore.types


def show_commands(message):
    out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    first_button = types.KeyboardButton('📒 Внести запис')
    second_button = types.KeyboardButton('📒 Переглянути записи')
    third_button = types.KeyboardButton('📒 Видалити запис')
    menu_button = types.KeyboardButton('📱 Головне меню')
    out_markup.add(first_button, second_button, third_button, menu_button)
    bot.send_message(message.chat.id, "\n📒 Меню записника\n",
                     parse_mode='html', reply_markup=out_markup)
    bot.delete_message(message.chat.id, message.message_id)
