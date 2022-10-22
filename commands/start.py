from core import botCore

bot = botCore.bot
me = botCore.me
types = botCore.types


def start(message, action):
    if action == "start":
        content = f'Привіт, <b>{message.from_user.username}</b>, ми раді, що Ви вирішили полегшити собі життя і ' \
                  f'скористатись цим ботом!\nВін створений спеціально для студентів університету <u>"НЛТУ ' \
                  f'ІДКТД"</u>\n\nОберіть знизу кнопку <u>📚 Команди</u>, щоб дізнатись можливості бота.\nБажаємо ' \
                  f'гарного дня ✨ '
    elif action == "menu":
        content = f'📱 Головне меню'

    out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    commands = types.KeyboardButton('📚 Команди')
    website_button = types.KeyboardButton('📄 Сайт Інституту')
    out_markup.add(commands, website_button)

    bot_message = bot.send_message(message.chat.id, content, parse_mode='html', reply_markup=out_markup)
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, bot_message.id - 2)
