import logging

from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from utils.notify_admins import comment


from loader import dp
from states.uzb_personalData import PersonalData
from keyboards.inline.uzb_menuKeyboards import  menu, informatsiya

@dp.callback_query_handler(text="vakansiya")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Qaysi yo'nalish bo'yicha ishlamoqchisiz:")
    await PersonalData.qaysi_sohaga.set()

@dp.message_handler(state=PersonalData.qaysi_sohaga)
async def answer_soha(message: Message, state: FSMContext):
    soha = message.text

    await state.update_data(
        {
            'soha tanlandi': soha
        }
    )
    await message.answer("To'liq ism sharifingizni kiriting:")
    await PersonalData.fullname.set()

@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {
            'F.I.O': fullname
        }
    )
    await message.answer("Rezyumeni yuboring:")
    await PersonalData.next()

@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=PersonalData.resume)
async def answer_resume(message: Message, state: FSMContext):
    resume = message.document

    await state.update_data(
        {
            'resume': resume.file_name
        }
    )
    await message.answer("Telefon raqamingizni yuboring:")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.phoneNumber)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {
            'telefon nomer': phone
        }
    )
    
    data = await state.get_data()
    soha = data.get('soha tanlandi')
    fullname = data.get('F.I.O')
    resume = data.get('resume')
    phone = data.get('telefon nomer')




    msg = (
        "Quyidagi ma'lumotlar qabul qilindi.\n"
        "Tez orada operatorlarimiz bog'lanadi.\n\n\n"
        f"<b>Topshirgan yo'nalshingiz</b>: {soha}\n"
        f"<b>ism familiya sharifi</b>: {fullname}\n"
        f"<b>Rezyumengiz</b>: {resume}\n"
        f"<b>Telefon raqamingiz</b>: {phone}"
    )

    
    await comment(msg)

    
    await state.finish()
    await state.reset_state(with_data=False)
    await message.answer(msg, reply_markup=informatsiya)

@dp.callback_query_handler(text="2ortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    await call.message.answer_photo(photo=photo, reply_markup=menu)
