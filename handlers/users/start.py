from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.tillar import tillar
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    photo = open("photos/tramplin.jpg",'rb')
    msg = f"""
    Assalomu alleykum hurmatli <b>{message.from_user.username}👨🏻‍💻</b>!\n<b>Tramplin</b>ga.\nXush kelibsiz🤝\n\nЗдравствуйте Уважаемый <b>{message.from_user.username}👨🏻‍💻</b>!\nДобро пожаловать на <b>Трамплин</b>\n\n<b>Tillni tanlang👇\nВыберите язык👇</b>
    """
    await message.answer_photo(photo=photo, caption=msg, reply_markup=tillar)

