from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

brain = MemoryStorage()
bot = Bot(token='TOKEN')
dp = Dispatcher(bot, storage=brain)
print("ONLINE")