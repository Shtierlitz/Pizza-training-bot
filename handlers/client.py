# F:\Python\TGBOT\Pizza-training-bot\handlers\client.py


from create_bot import dp
from keyboards import kb_client  # импорт клавиатуры
from aiogram.types import ReplyKeyboardRemove
from aiogram import types, Dispatcher


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        # await bot.send_message(message.from_user.id, "Приятного аппетита")
        await message.reply("Начинаем!", reply_markup=kb_client)  # Добавляем клавиатуру
        await message.delete()
    except Exception as e:
        await message.reply(f"Ошибка: {e}\n Общение с ботом через ЛС, напишите ему: \nhttps://t.me/Pizza_Shtir_bot")


# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    # await bot.send_message(message.from_user.id, "Вс-Чт с 9:00 до 20:00б Пт-Сб с 10:00 до 23:00")
    await message.reply("Вс-Чт с 9:00 до 20:00б Пт-Сб с 10:00 до 23:00")


# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    # await bot.send_message(message.from_user.id, "Киев, пр.Королева 2В")
    await message.reply("Киев, пр.Королева 2В")  # reply_markup=ReplyKeyboardRemove() - удалит клаву после ввода


async def pur_zayka(message: types.Message):
    await message.reply("Мур мур зайка! 😘")


# Хендлер для отлавливания конкретного слова
# @dp.message_handler(lambda message: "Такси" in message.text)
async def taxi(message: types.Message):
    await message.answer("Такси")


# @dp.message_handler(commands=['Меню'])
# async def pizza_open_command(message: types.Message):
#     for ret in cur.execute('SELECT * FROM menu').fetchall():
#         await bot.send_photo(message.from_user.id, ret[0], f"{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}")

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, lambda message: message.text.lower() == "режим работы 🕐")
    dp.register_message_handler(pizza_place_command, lambda message: message.text.lower() == "расположение 📍")
    dp.register_message_handler(pur_zayka, lambda message: message.text.lower() == "мур 😺")
    dp.register_message_handler(taxi, lambda message: "такси" in message.text.lower())

