# F:\Python\TGBOT\keyboards\client_kb.py
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton("/Режим_работы")  # кнопки по отдельности
b2 = KeyboardButton("/Меню")
b3 = KeyboardButton("/Расположение")
pur = KeyboardButton("/мур")
# b4 = KeyboardButton("Поделиться номером", request_contact=True)
# b5 = KeyboardButton("Отправить где я", request_location=True)



kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  # Замещает клаву обыную на нашу
# resize_keyboard - меняет размер кнопок под размер текста
# one_time_keyboard - прячет клавиатуру после того как нажал на кнопку

# kb_client.add(b1).add(b2).insert(b3)  # добавляем кнопки в клаву
# add - добавляет кнопку снизу
# insert - добавляет кнопку справа в ряд
# row - делает все кнопки из аргументов в одну строку

kb_client.row(b1, b2, b3, pur)


