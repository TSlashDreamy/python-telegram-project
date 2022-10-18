import math
import schedule
from datetime import date
from core import botCore
from commands import start as bot_start
from commands import website as bot_website
from commands import commandsList as bot_help
from commands import dateCheck as bot_date
from commands import schedulesList as bot_allSchedules
from commands import showSchedule as bot_showSchedule

bot = botCore.bot

global even_week


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
schedule.every().tuesday.at("14:07").do(calculate_even_week)

# calculate after reboot
calculate_even_week()


# handler - listening to user commands
@bot.message_handler(commands=['start', 'menu'])
def start(message):
    bot_start.start(message)
    # !!!BONE, FIX NEEDED!!!
    while True:
        schedule.run_pending()


@bot.message_handler(commands=['website'])
def website(message):
    bot_website.website(message)


@bot.message_handler(content_types=['text'])
def get_commands(message):
    global even_week

    if message.text == "📚 Commands":
        bot_help.show_commands(message)

    if message.text == "📅 Check date status":
        bot_date.date_check(message, even_week)

    if message.text == "📃 Schedules":
        bot_allSchedules.get_available_schedules(message)

    if message.text == "КНС-11/1" \
            or message.text == "КНС-11/2" \
            or message.text == "КНС-12" \
            or message.text == "КНС-21/1" \
            or message.text == "КНС-21/2":
        bot_showSchedule.show_shedule(message, even_week)


bot.infinity_polling()
