# F:\Python\TGBOT\Pizza-training-bot\handlers\other.py

import json, string

from aiogram import types, Dispatcher

import os

# Получить путь к текущему файлу
current_file_path = os.path.realpath(__file__)

# Получить директорию текущего файла
current_dir = os.path.dirname(current_file_path)

# Перейти на уровень вверх
parent_dir = os.path.dirname(current_dir)

# Создать абсолютный путь к файлу
file_path = os.path.join(parent_dir, 'cenz.json')


# @dp.message_handler()  # отлавливает когда кто-то что-то пишет
# async def echo_send(message: types.message):
#     if message.text == 'Привет':
#         await message.answer("И тебе приет!)")
#     # await message.answer(message.text)  # отвечает в группу
#     # await message.reply(message.text)  # упоминает сообщение на которое отвечает
#     # await bot.send_message(message.from_user.id, message.text)  # отвечает личным сообщением пользователю

# @dp.message_handler()
async def echo_cenz_filter(message: types.message):  # функция фильтра от мата
    user_words = {i.lower().translate(str.maketrans("", "", string.punctuation))
                  for i in message.text.split(" ") if len(i) > 1}
    censored_words = set(json.load(open(file_path)))

    if user_words.intersection(censored_words):
        await message.reply("Маты запрещены!")
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_cenz_filter)
