import telebot

API_TOKEN = 'Nope'
bot = telebot.TeleBot(API_TOKEN)
me = bot.get_me()

print(f'logged in: {me.first_name}')


# handler - listening to user commands
@bot.message_handler(commands=['start'])
def start(message):
    content = f'Hi, {message.from_user.username} i`m working!'
    bot.send_message(message.chat.id, content, parse_mode='html')


bot.infinity_polling()
