from aiogram import executor
from data.config import ADMINS
from loader import dp, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import asyncio
import aioschedule
from aiogram import types
import os




from art import tprint as t

async def send_database():
	file = types.InputFile(path_or_bytesio = "data/main.db")
	await bot.send_document(chat_id = ADMINS[0], document = file, caption = "Database 🗄")

async def daily_tasks():
	aioschedule.every(12).hours.do(send_database)
    
	while True:
		await aioschedule.run_pending()
		await asyncio.sleep(1)
    



async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)
    t("cod1ng_now")
    t("kanaliga")
    t("obuna")
    t("bo'ling")
    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)
    asyncio.create_task(daily_tasks())
    


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
