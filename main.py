import schedule
from core import botCore
from core import dateCalculation
from commands import start as bot_start, diaryCheck
from commands import website as bot_website
from commands import showSchedule as bot_showSchedule
from commands import commandsList, back, dateCheck, schedulesList, menu, diaryTrigger, diaryRemember, diaryList, diaryDelete

bot = botCore.bot

dateCalculation.calculate_even_week()

# calculate every monday at 00:00
schedule.every().monday.at("00:00").do(dateCalculation.calculate_even_week)


# handler - listening to user commands
@bot.message_handler(commands=['start'])
def start(message):
    bot_start.start(message, "start")
    # inject schedule cycle into bot.infinity_polling() (Prevents conflict)
    while True:
        schedule.run_pending()


@bot.message_handler(content_types=['text'])
def get_commands(message):
    if diaryTrigger.inputting_note:
        diaryRemember.remember_data(message)

    if diaryDelete.deleting_note:
        diaryDelete.delete_note(message)

    if message.text == "📚 Команди":
        commandsList.show_commands(message)

    if message.text == "📱 Головне меню":
        menu.show(message)

    if message.text == "🔙 Назад":
        back.back(message)

    if message.text == "📄 Сайт Інституту":
        bot_website.website(message)

    if message.text == "📅 Точна дата":
        dateCheck.date_check(message)

    if message.text == "📒 Записник":
        diaryList.show_commands(message)

    if message.text == "📒 Внести запис":
        diaryTrigger.trigger_event(message)

    if message.text == "📒 Переглянути записи":
        diaryCheck.show_notes(message)

    if message.text == "📒 Видалити запис":
        diaryDelete.delete_note(message)

    if message.text == "📃 Розклад":
        schedulesList.get_available_schedules(message)

    if message.text == "КНС-11/1" \
            or message.text == "КНС-11/2" \
            or message.text == "КНС-12" \
            or message.text == "КНС-21/1" \
            or message.text == "КНС-21/2":
        bot_showSchedule.show_shedule(message, dateCalculation.even_week)


bot.infinity_polling()
