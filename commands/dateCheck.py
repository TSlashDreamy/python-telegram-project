from commands import commandsList
from core import botCore, dateCalculation, daySwitcher

bot = botCore.bot
me = botCore.me
types = botCore.types


def represent_bool_variable(inner):
    if not inner:
        return "не парний "
    elif inner:
        return "парний"


def date_check(message):
    dateCalculation.calculate_even_week()
    message_list = [f'\nЧас: {str(dateCalculation.time)}',
                    f'День тижня: {str(daySwitcher.switch_day(dateCalculation.day))}',
                    f'Сьогоднішня дата: {str(dateCalculation.today.strftime("%d/%m/%Y"))}',
                    f'Всього днів пройшло: {str(dateCalculation.days.days)}',
                    f'Всього тижнів пройшло: {str(dateCalculation.weeks)}',
                    f'Тиждень: <u>{str(represent_bool_variable(dateCalculation.even_week))}</u>'
                    ]

    bot_message = bot.send_message(message.chat.id, f"🗓️ Сьогодні: \n" + "\n".join(message_list), parse_mode='html')
    bot.delete_message(message.chat.id, message.id)
    bot.delete_message(message.chat.id, bot_message.id - 2)
    commandsList.show_commands(message, "call")
