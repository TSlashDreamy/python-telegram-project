from commands import diaryList, diaryTrigger
from core import botCore, dateCalculation
from diary_notes import getDiaryData, setDiaryData

global number
number = 0

bot = botCore.bot
me = botCore.me
types = botCore.types


def remember_data(message):
    global number
    current_date = dateCalculation.today.strftime("%d/%m/%Y")
    data = getDiaryData.get_data()
    if data != 0:
        for i in range(len(data)):
            i+=1
            number = i
    else:
        number = 0

    setDiaryData.database_input(number + 1, message.text, current_date, message.from_user.id)
    bot.send_message(message.chat.id, "✅ Запис внесено",
                     parse_mode='html')
    diaryTrigger.inputting_note = False
    diaryList.show_commands(message)
