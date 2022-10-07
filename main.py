import telebot
from telebot import types

API_TOKEN = 'nope'
bot = telebot.TeleBot(API_TOKEN)
me = bot.get_me()

print(f'logged in: {me.first_name}')


# handler - listening to user commands
@bot.message_handler(commands=['start'])
def start(message):
    content = f'Hi, <b>{message.from_user.username}</b> i`m working!\n<u>(Buttons not working now)</u>'
    out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    commands = types.KeyboardButton('📚 Commands')
    website_button = types.KeyboardButton('/website')
    out_markup.add(commands, website_button)

    bot.send_message(message.chat.id, content, parse_mode='html', reply_markup=out_markup)


@bot.message_handler(commands=['website'])
def website(message):
    in_markup = types.InlineKeyboardMarkup()
    website_link = types.InlineKeyboardButton('Веб-сайт ІДТКД', url='https://idtd.nltu.edu.ua/')
    in_markup.add(website_link)

    bot.send_message(message.chat.id, "Website link", parse_mode='html', reply_markup=in_markup)


@bot.message_handler(content_types=['text'])
def get_commands(message):
    if message.text == "📚 Commands":
        bot.send_message(message.chat.id, "Whoops, working on it", parse_mode='html')


bot.infinity_polling()
