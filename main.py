import telebot
import os
from telebot import types
from dotenv import load_dotenv
from PythonApplication1 import get_monday_shedule, get_all_shedule

load_dotenv()

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
me = bot.get_me()

global even_week
even_week = False
print(f'Logged in Succesfully ✅'
      f'\nName: {me.first_name}'
      f'\nID: {me.id}'
      f'\nBot account: {me.is_bot}'
      f'\nBot link: https://t.me/{me.username}')


# handler - listening to user commands
@bot.message_handler(commands=['start', 'menu'])
def start(message):
    content = f'Hi, <b>{message.from_user.username}</b> i`m working!\nPress <u>📚 Commands</u> for available commands'
    out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    commands = types.KeyboardButton('📚 Commands')
    website_button = types.KeyboardButton('/website')
    switcher_button = types.KeyboardButton('🔳 Switch even week')
    out_markup.add(commands, website_button, switcher_button)

    bot.send_message(message.chat.id, content, parse_mode='html', reply_markup=out_markup)


@bot.message_handler(commands=['website'])
def website(message):
    in_markup = types.InlineKeyboardMarkup()
    website_link = types.InlineKeyboardButton('Веб-сайт ІДТКД', url='https://idtd.nltu.edu.ua/')
    in_markup.add(website_link)

    bot.send_message(message.chat.id, "Website link", parse_mode='html', reply_markup=in_markup)


@bot.message_handler(content_types=['text'])
def get_commands(message):
    global even_week, name
    if message.text == "📚 Commands":
        out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        shedule_button = types.KeyboardButton('📃 Shedules')
        out_markup.add(shedule_button)
        bot.send_message(message.chat.id, "Choose what you want by pressing a button",
                         parse_mode='html', reply_markup=out_markup)

    if message.text == "🔳 Switch even week":
        if even_week:
            even_week = False
        else:
            even_week = True

        bot.send_message(message.chat.id, f"Switched to <u>{str(even_week)}</u>",
                         parse_mode='html')

    if message.text == "📃 Shedules":
        out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        first_button = types.KeyboardButton('КНС-11/1')
        second_button = types.KeyboardButton('КНС-11/2')
        out_markup.add(first_button, second_button)
        bot.send_message(message.chat.id, "Choose your group",
                         parse_mode='html', reply_markup=out_markup)

    if message.text == "КНС-11/1":
        bot.send_message(message.chat.id, "Working on it",
                         parse_mode='html')

    if message.text == "КНС-11/2":
        out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu_button = types.KeyboardButton('/menu')
        out_markup.add(menu_button)
        all_shedules = get_all_shedule()
        shedule_list = []
        for i in range(len(all_shedules)):
            day = switch_day(i)
            shedule_list.append(day)
            for y in range(len(all_shedules[i])):
                number = all_shedules[i][y][0]
                name = all_shedules[i][y][1]
                if "/" in all_shedules[i][y][1]:
                    if even_week:
                        name = all_shedules[i][y][1].split("/", 1)[1]
                    else:
                        name = all_shedules[i][y][1].split("/", 1)[0]
                time = all_shedules[i][y][2]
                content = str(number) + ". " + name + " " + str(time)
                shedule_list.append(content)

        print(shedule_list)
        bot.send_message(message.chat.id, "\n".join(shedule_list),
                         parse_mode='html', reply_markup=out_markup)
        if even_week:
            bot.send_message(message.chat.id, "Тиждень <u>парний</u>",
                         parse_mode='html')
        else:
            bot.send_message(message.chat.id, "Тиждень <u>не парний</u>",
                             parse_mode='html')


def switch_day(inner):
    match inner:
        case 0:
            return "\nMonday\n================================="

        case 1:
            return "\nTuesday\n================================="

        case 2:
            return "\nWednesday\n================================="

        case 3:
            return "\nThursday\n================================="

        case 4:
            return "\nFriday\n================================="


bot.infinity_polling()
