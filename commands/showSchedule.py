from core import botCore
from PythonApplication1 import get_all_schedule
from core import daySwitcher
from core import scheduleSwitcher

bot = botCore.bot
me = botCore.me
types = botCore.types


def show_shedule(message, even_week):
    try:
        group = "Group: " + message.text
        out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        menu_button = types.KeyboardButton('/menu')
        out_markup.add(menu_button)
        all_schedules = get_all_schedule(scheduleSwitcher.switch_schedule(message.text))
        schedule_list = [group]
        for i in range(len(all_schedules)):
            day = daySwitcher.switch_day(i)
            schedule_list.append(day)
            for y in range(len(all_schedules[i])):
                number = all_schedules[i][y][0]
                name = all_schedules[i][y][1]
                if "/" in all_schedules[i][y][1]:
                    if even_week:
                        name = all_schedules[i][y][1].split("/", 1)[1]
                    else:
                        name = all_schedules[i][y][1].split("/", 1)[0]
                time = all_schedules[i][y][2]
                content = str(number) + ". " + name + " " + str(time)
                schedule_list.append(content)

        print(schedule_list)
        bot.send_message(message.chat.id, "\n".join(schedule_list),
                         parse_mode='html', reply_markup=out_markup)
        if even_week:
            bot.send_message(message.chat.id, "Тиждень <u>парний</u>", parse_mode='html')
        else:
            bot.send_message(message.chat.id, "Тиждень <u>не парний</u>",
                             parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)
    except:
        bot.send_message(message.chat.id, "На жаль розкладу для вашої групи поки-що немає :с",
                         parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)
