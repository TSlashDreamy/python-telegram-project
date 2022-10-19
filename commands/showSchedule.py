from core import botCore, scheduleSwitcher, daySwitcher, dateCalculation, lessonSwitcher
from databases.databaseManagment import get_all_schedule

bot = botCore.bot
me = botCore.me
types = botCore.types


def show_shedule(message, even_week):
    # recalculating all variables
    dateCalculation.calculate_even_week()
    try:
        group = "Група: " + message.text
        # buttons
        out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        back_button = types.KeyboardButton('🔙 Назад')
        menu_button = types.KeyboardButton('📱 Головне меню')
        out_markup.add(back_button, menu_button)
        # getting DB
        all_schedules = get_all_schedule(scheduleSwitcher.switch_schedule(message.text))
        schedule_list = [group]
        # getting schedules from DB
        for i in range(len(all_schedules)):
            # injecting day
            day = daySwitcher.switch_day(i)
            # checking what day today and highlighting it
            if dateCalculation.day == i:
                schedule_list.append(f'\n➡️ <b><u>Сьогодні - {day}</u>\n=================================</b>')
            else:
                schedule_list.append(f'\n{day}\n=================================')
            # getting data from DB list
            for y in range(len(all_schedules[i])):
                number = all_schedules[i][y][0]
                name = all_schedules[i][y][1]
                # getting schedule by the even week
                if "/" in all_schedules[i][y][1]:
                    if even_week:
                        name = all_schedules[i][y][1].split("/", 1)[1]
                    else:
                        name = all_schedules[i][y][1].split("/", 1)[0]
                time = all_schedules[i][y][2]
                # checking current lesson and highlighting it
                if lessonSwitcher.select_current(number - 1) and dateCalculation.day == i:
                    content = f'▶️ <b><u>{str(number)}. {name} {str(time)}</u></b>'
                elif not lessonSwitcher.select_current(number - 1):
                    content = f'{str(number)}. {name} {str(time)}'
                schedule_list.append(content)

        # sending message to user
        bot.send_message(message.chat.id, "\n".join(schedule_list),
                         parse_mode='html', reply_markup=out_markup)
        if even_week:
            bot.send_message(message.chat.id, "Тиждень <u>парний</u>", parse_mode='html')
        else:
            bot.send_message(message.chat.id, "Тиждень <u>не парний</u>",
                             parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)
    # catching errors
    except Exception as e:
        print(f"⚠️Oh noes, we got an error while trying to show schedule: {repr(e)}")
        bot.send_message(message.chat.id, "На жаль розкладу для вашої групи поки-що немає :с",
                         parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)
