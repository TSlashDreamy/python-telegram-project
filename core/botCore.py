import logging

import telebot
import os
from telebot import types
from dotenv import load_dotenv

load_dotenv()

status = "✅ Успішний вхід в API Telegram"

try:
    API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
    bot = telebot.TeleBot(API_TOKEN)
    me = bot.get_me()
    types = types
    owner_id = int(os.getenv("OWNER_ID"))
    print("\n========================\n")
    print(f'📃 Telegram Log: '
          f'\n{status}'
          f'\n📃 Назва бота: {me.first_name}'
          f'\n🆔 ID: {me.id}'
          f'\n🤖 Аккаунт бота?: {me.is_bot}'
          f'\n🔗 Посилання на бота: https://t.me/{me.username}')
except Exception as e:
    status = "❌🔐 Здається, Ваш токен не правильний"
    logging.error(e)
    print("\n========================\n")
    print(f'📃 Telegram Log: '
          f'\n{status}')
