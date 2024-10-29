import logging

from aiogram import Dispatcher
from data.config import ADMINS
from loader import dp

async def comment(msg):
    for i in ADMINS:
        await dp.bot.send_message(chat_id=i, text=msg)

async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot ishga tushdi")

        except Exception as err:
            logging.exception(err)
