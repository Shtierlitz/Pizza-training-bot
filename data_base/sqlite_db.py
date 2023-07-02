# F:\Python\TGBOT\Pizza-training-bot\data_base\sqlite_db.py
import os
import sqlite3 as sq
from create_bot import dp, bot


def sql_start():
    global base, cur
    current_dir = os.path.dirname(__file__)  # текущая директория скрипта
    parent_dir = os.path.dirname(current_dir)  # директория на уровень выше
    db_path = os.path.join(parent_dir, 'pizza_cool.db')  # формируем путь к базе данных

    base = sq.connect(db_path)
    cur = base.cursor()
    if base:
        print("data base connected OK!")
    base.execute("CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)")
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO menu VALUES (?, ?, ?, ?)", tuple(data.values()))
        base.commit()


async def sql_read(message):
    print("sql_read")
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.chat.id, ret[0], f"{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}")


async def sql_read2():
    return cur.execute('SELECT * from menu ').fetchall()


async def sql_delete_command(data):
    cur.execute("DELETE FROM menu WHERE name == ?", (data,))
    base.commit()


