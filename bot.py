from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

from config import TOKEN, ADMIN_ID

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_cmd(message: Message):
	await message.answer("Приветствуем тебя в официальном боте кафедры мировой экономики РЭУ им. Г.В.Плеханова !\nЧто умеет этот бот?\n✅ присылайте ваши вопросы для рубрики вопрос/ответ (после проверки модераторами они будут опубликованы)")


@dp.message_handler()
async def start_cmd(message: Message):
	await message.answer("Вопрос получен ✅ после проверки он будет опубликован")
	await bot.send_message(ADMIN_ID, text=message.text)


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
