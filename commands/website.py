from core import botCore

bot = botCore.bot
me = botCore.me
types = botCore.types


def website(message):
    in_markup = types.InlineKeyboardMarkup()
    website_link = types.InlineKeyboardButton('Веб-сайт ІДТКД', url='https://idtd.nltu.edu.ua/')
    in_markup.add(website_link)

    bot.send_message(message.chat.id, "Натисніть на кнопку, щоб перейти на сайт",
                     parse_mode='html',
                     reply_markup=in_markup)
    bot.delete_message(message.chat.id, message.message_id)
