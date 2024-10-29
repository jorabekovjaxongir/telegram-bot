from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)



    # print(f"\x1b[32m[USER]:\x1b[0m{message.from_user.full_name},\x1b[32m[ID]:\x1b[0m{message.from_user.id}",end=",")
    # print(f"\x1b[32m[Text]:\x1b[0m{message.text}")