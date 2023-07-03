from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os, hashlib

from aiogram.types import InputTextMessageContent, InlineQueryResultArticle
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.environ.get('TOKEN'))  # читаем токен
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_hendler(query: types.InlineQuery):
    text: str = query.query or "echo"
    link = 'https://ru.wikipedia.org/wiki/' + "_".join(text.split(" "))
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title='Статья Wikipedia:',
        url=link,
        input_message_content=types.InputTextMessageContent(
            message_text=link
        )
    )]
    await query.answer(articles, cache_time=1, is_personal=True)


executor.start_polling(dp, skip_updates=True)
