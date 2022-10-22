from commands import commandsList
from core import botCore

global schedule_running, activated
schedule_running = False
activated = False

bot = botCore.bot


def switch_updating(message):
    global schedule_running, activated
    if message.from_user.id == botCore.owner_id and not schedule_running:
        schedule_running = True
        activated = True
        bot_message = bot.send_message(message.chat.id, f"✅ Увімкнено динамічне оновлення даних", parse_mode='html')
        bot.delete_message(message.chat.id, message.id)
        bot.delete_message(message.chat.id, bot_message.id - 2)
        commandsList.show_commands(message, "call")
    elif schedule_running:
        activated = False
        bot_message = bot.send_message(message.chat.id, f"⭕ Динамічне оновлення даних уже працює", parse_mode='html')
        bot.delete_message(message.chat.id, message.id)
        bot.delete_message(message.chat.id, bot_message.id - 2)
        commandsList.show_commands(message, "call")
