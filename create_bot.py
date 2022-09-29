from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

brain = MemoryStorage()
bot = Bot(token='TOKEN')
dp = Dispatcher(bot, storage=brain)
print("ONLINE")