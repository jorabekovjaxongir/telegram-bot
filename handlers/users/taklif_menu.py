from aiogram import types
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext
from utils.notify_admins import comment


from loader import dp
from states.takliflar import PersonalData3
from keyboards.inline.uzb_menuKeyboards import  menu, shikoyat_menu

@dp.callback_query_handler(text="shikoyat_takliflar")
async def enter_text(call: CallbackQuery):
    await call.message.answer("Takliflar va shikoyatlar kiriting!")
    await call.message.delete()
    await PersonalData3.fullname.set()

@dp.message_handler(state=PersonalData3.fullname)
async def answer_soha(message: Message, state: FSMContext):


    text = message.text
    await state.update_data(
        {
            'name': text
        }
    )
    await message.answer("Telefon raqamingizni kiriting:")
    # await message.delete()
    await PersonalData3.next()

@dp.message_handler(state=PersonalData3.phoneNumber)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {
            'telefon_nomer': phone
        }
    )
    
    data = await state.get_data()
    fullname = data.get('name')
    phone = data.get('telefon_nomer')

    msg = f"""
        Quyidagi ma'lumotlar qabul qilindi.\n
        Tez orada operatorlarimiz bog'lanadi.\n\n\n
        <b>Taklif va shikoyat</b>: {fullname}\n
        <b>Telefon raqamingiz</b>: {phone}
    """

    await comment(msg)

    
    # await message.delete()
    await state.finish()
    await message.answer(msg, reply_markup=shikoyat_menu)

@dp.callback_query_handler(text="1shikoyatortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    msg = "<b>Меню:</b>"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=menu)
