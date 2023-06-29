# F:\Python\TGBOT\create_bot.py

import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()   # хранилище блока состояния

bot = Bot(token=os.getenv('TOKEN'))  # читаем токен
dp = Dispatcher(bot, storage=storage)  #