from core import botCore
from datetime import date


bot = botCore.bot
me = botCore.me
types = botCore.types


def date_check(message, even_week):
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
