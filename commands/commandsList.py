from admin import dynamicUpdate
from core import botCore

bot = botCore.bot
me = botCore.me
types = botCore.types


def show_commands(message, call="null"):
    out_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    schedule_button = types.KeyboardButton('📃 Розклад')
    date_button = types.KeyboardButton('📅 Точна дата')
    diary_button = types.KeyboardButton('📒 Записник')
    out_markup.add(schedule_button, date_button, diary_button)
    if message.from_user.id == botCore.owner_id:
        if not dynamicUpdate.schedule_running:
            out_markup.add('❌ Динамічне оновлення не запущено')
        else:
            out_markup.add('✅ Динамічне оновлення працює')
    bot.send_message(message.chat.id, "Оберіть бажану команду однією з кнопок нижче",
                     parse_mode='html', reply_markup=out_markup)
    if call == "null":
        bot.delete_message(message.chat.id, message.message_id)
