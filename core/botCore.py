import telebot
import os
from telebot import types
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
me = bot.get_me()
types = types

print(f'📃 Telegram Log: '
      f'\nLogged in Successfully ✅'
      f'\nName: {me.first_name}'
      f'\nID: {me.id}'
      f'\nBot account: {me.is_bot}'
      f'\nBot link: https://t.me/{me.username}')