from commands import diaryList
from core import botCore
from diary_notes import getDiaryData

bot = botCore.bot
me = botCore.me
types = botCore.types


def show_notes(message):
    try:
        diary_data = getDiaryData.get_data()
        diary_list = []
        for i in range(len(diary_data)):
            if diary_data[i][1] == message.from_user.id:
                content = f'{diary_data[i][0]}. <b>{diary_data[i][2]}</b>   📆{diary_data[i][3]}'
                diary_list.append(content)
        bot.send_message(message.chat.id, "\n".join(diary_list),
                         parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)
    except Exception:
        bot.send_message(message.chat.id, "📂 У Вас немає записів",
                         parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)
