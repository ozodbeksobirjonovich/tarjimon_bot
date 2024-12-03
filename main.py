from pytarjimon import tarjima

from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="8119520916:AAEaMXwsQ90BB3640V5FswDVsxVOPptDIhM")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def startprocess(message: types.Message):
    await message.answer("Salom! Tarjimon botiga xush kelibsiz! Xabaringizni yozing...")

@dp.message_handler(content_types=["text"])
async def translateprocess(message: types.Message):
    uz = tarjima(text=message.text, language="uz")
    ru = tarjima(text=message.text, language="ru")
    en = tarjima(text=message.text, language="en")
    await message.reply(
        f"🇺🇿 O'zbekcha: {uz}\n"
        f"🇷🇺 Русский: {ru}\n"
        f"🇺🇸 English: {en}"
    )

executor.start_polling(dp)