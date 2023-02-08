import logging
import time
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot_config import TOKEN_API

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN_API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Connection to DB
con = sqlite3.connect('/home/tretyakov/PycharmProjects/PriceProject/phones.db')
cursor = con.cursor()


class UserChoice(StatesGroup):
    user_choice = State()


# Greetings user
@dp.message_handler(commands=['start'])
async def greeting_user(message: types.Message):
    await message.reply("Здравствуйте! Я бот для поиска мобильных телефонов по выгодным ценам.")
    time.sleep(2)
    await message.reply('Пожалуйста укажите марку и модель искомого телефона, к примеру "Samsung Galaxy A33" или '
                        '"iPhone 13" ')


@dp.message_handler()
async def phone_model(message: types.Message, state: FSMContext):
    await message.answer('Идёт поск, пожалуйста подождите немного.')

    user_model = message.text
    query = f"""SELECT model FROM rozetka WHERE model LIKE '%{user_model}%'  
                UNION 
                SELECT model FROM q_techno WHERE model LIKE '%{user_model}%'"""
    cursor.execute(query)
    button_names = cursor.fetchall()
    time.sleep(1.500)

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for btn in button_names:
        kb.add(KeyboardButton(btn[0]))
    await message.answer(text="Вибирите модель из приведённых ниже:",
                         reply_markup=kb)
    await UserChoice.user_choice.set()


@dp.message_handler(state=UserChoice.user_choice)
async def user_chosen(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        url_query = f"""SELECT url FROM rozetka WHERE model LIKE '%{user_message}%'  
                UNION 
                SELECT url FROM q_techno WHERE model LIKE '%{user_message}%'"""
        cursor.execute(url_query)
        url = cursor.fetchall()
        await message.reply(f"Вот ваша ссылка: {url[0]}")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
