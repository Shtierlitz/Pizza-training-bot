# F:\Python\TGBOT\handlers\admin.py
from aiogram import types, Dispatcher


from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# Начало диалога загрузки пункта меню
# @dp.message_handler(commands="Загрузить", state=None)
async def cm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply("Загрузить фото")


# Ловим первый ответ и пишем в словарь
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply("Теперь введи название")


# Ловим второй ответ
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply("Теперь введи описание")


# Ловим третий ответ
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply("Теперь введи цену")


# Ловим четвертый ответ
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)

    async with state.proxy() as data:
        await message.reply(str(data))

    # до этой строки выполняется все операции с данными
    await state.finish()


# Регистрируем хендлеры
def register_hendlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(load_photo, content_types=types.ContentType.PHOTO, state=FSMAdmin.photo)
    dp.register_message_handler(load_name, content_types=types.ContentType.TEXT, state=FSMAdmin.name)
    dp.register_message_handler(load_description, content_types=types.ContentType.TEXT, state=FSMAdmin.description)
    dp.register_message_handler(load_price, content_types=types.ContentType.TEXT, state=FSMAdmin.price)

