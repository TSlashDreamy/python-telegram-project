from core import botCore
import schedule

bot = botCore.bot
me = botCore.me
types = botCore.types


def start(message):
    content = f'Hi, <b>{message.from_user.username}</b> i`m working!\nPress <u>📚 Commands</u> for available commands'
    out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    commands = types.KeyboardButton('📚 Commands')
    website_button = types.KeyboardButton('/website')
    out_markup.add(commands, website_button)

    bot.send_message(message.chat.id, content, parse_mode='html', reply_markup=out_markup)
    bot.delete_message(message.chat.id, message.message_id)
    # inject schedule cycle into bot.infinity_polling() (Prevents conflict)
    while True:
        schedule.run_pending()
