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
    count = 0
    current_date = dateCalculation.today.strftime("%d/%m/%Y")
    data = getDiaryData.get_data()
    if diaryTrigger.input_for_user == message.from_user.id:
        if data != 0:
            number = 0
            for i in range(len(data)):
                if data[i][1] == message.from_user.id:
                    count += 1
                    i += 1
                    number = i

        else:
            number = 0
    else:
        return
    setDiaryData.database_input(count + 1, message.text, current_date, message.from_user.id)
    bot_message = bot.send_message(message.chat.id, "✅ Запис внесено",
                     parse_mode='html')
    bot.delete_message(message.chat.id, message.id)
    bot.delete_message(message.chat.id, bot_message.id - 2)
    diaryTrigger.input_for_user = 0
    diaryTrigger.inputting_note = False
    diaryList.show_commands(message, "call")
