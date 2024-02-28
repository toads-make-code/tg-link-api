import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Объект бота
bot = Bot(token="6059249584:AAHpv997wcDRM0aksMMGuhQGTJ5qxIsK7dk")
# Диспетчер
dp = Dispatcher()

class DeviceState(StatesGroup):
    add_new_device = State()
    control_device = State()
    select_device = State()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Вве")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)