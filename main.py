import telebot
import os
import math
import schedule
from datetime import date
from telebot import types
from dotenv import load_dotenv
from PythonApplication1 import get_all_shedule

load_dotenv()

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
me = bot.get_me()

global even_week

print(f'📃 Telegram Log: '
      f'\nLogged in Successfully ✅'
      f'\nName: {me.first_name}'
      f'\nID: {me.id}'
      f'\nBot account: {me.is_bot}'
      f'\nBot link: https://t.me/{me.username}')


def calculate_even_week():
    global even_week

    days_a_week = 7
    today = date.today()
    start_year = date(date.today().year, 1, 1)
    days = today - start_year
    weeks = days.days / days_a_week
    weeks = math.floor(weeks)

    print("\n========================")
    print("🧮 Date calculating: ")
    print("🗓️ Today's date:", today.strftime("%d/%m/%Y"))
    print("📆 Total days:", days.days)
    print("📆 Total weeks:", weeks)

    if weeks % 2 == 0:
        print("Парний тиждень")
        even_week = True
    else:
        print("Не парний тиждень")
        even_week = False


# calculate every monday at 00:00
schedule.every().monday.at("00:00").do(calculate_even_week)


# calculate after reboot
calculate_even_week()


# handler - listening to user commands
@bot.message_handler(commands=['start', 'menu'])
def start(message):
    content = f'Hi, <b>{message.from_user.username}</b> i`m working!\nPress <u>📚 Commands</u> for available commands'
    out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    commands = types.KeyboardButton('📚 Commands')
    website_button = types.KeyboardButton('/website')
    switcher_button = types.KeyboardButton('📅 Check date status')
    out_markup.add(commands, website_button, switcher_button)

    bot.send_message(message.chat.id, content, parse_mode='html', reply_markup=out_markup)
    bot.delete_message(message.chat.id, message.message_id)
    # inject schedule cycle into bot.infinity_polling() (Prevents conflict)
    while True:
        schedule.run_pending()


@bot.message_handler(commands=['website'])
def website(message):
    in_markup = types.InlineKeyboardMarkup()
    website_link = types.InlineKeyboardButton('Веб-сайт ІДТКД', url='https://idtd.nltu.edu.ua/')
    in_markup.add(website_link)

    bot.send_message(message.chat.id, "Website link", parse_mode='html', reply_markup=in_markup)
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=['text'])
def get_commands(message):
    global even_week
    if message.text == "📚 Commands":
        out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        shedule_button = types.KeyboardButton('📃 Schedules')
        out_markup.add(shedule_button)
        bot.send_message(message.chat.id, "Choose what you want by pressing a button",
                         parse_mode='html', reply_markup=out_markup)
        bot.delete_message(message.chat.id, message.message_id)

    if message.text == "📅 Check date status":
        days_a_week = 7
        today = date.today()
        start_year = date(date.today().year, 1, 1)
        days = today - start_year
        weeks = days.days / days_a_week
        weeks = round(weeks)
        message_list = ["Today: " + str(today.strftime("%d/%m/%Y")),
                        "Total days: " + str(days.days),
                        "Total weeks: " + str(weeks),
                        "Even week: " + str(even_week)]

        bot.send_message(message.chat.id, f"📅 Info about date: \n" + "\n".join(message_list))
        bot.delete_message(message.chat.id, message.message_id)

    if message.text == "📃 Schedules":
        out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        first_button = types.KeyboardButton('КНС-11/1')
        second_button = types.KeyboardButton('КНС-11/2')
        out_markup.add(first_button, second_button)
        bot.send_message(message.chat.id, "Choose your group",
                         parse_mode='html', reply_markup=out_markup)
        bot.delete_message(message.chat.id, message.message_id)

    if message.text == "КНС-11/1":
        bot.send_message(message.chat.id, "Working on it",
                         parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)

    if message.text == "КНС-11/2":
        # calculate_even_week() - we don't need this anymore
        group = "Group: " + message.text
        out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu_button = types.KeyboardButton('/menu')
        out_markup.add(menu_button)
        all_shedules = get_all_shedule()
        shedule_list = [group]
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
            bot.send_message(message.chat.id, "Тиждень <u>парний</u>", parse_mode='html')
        else:
            bot.send_message(message.chat.id, "Тиждень <u>не парний</u>",
                             parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)


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
