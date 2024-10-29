
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext

from loader import dp
from states.uzb_anketaData import PersonalData1
from keyboards.inline.uzb_menuKeyboards import  kurslarmenu, anketa1
from utils.notify_admins import comment


@dp.callback_query_handler(text="anketa")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("To'liq ismingizni kiriting")
    await PersonalData1.fullname.set()

@dp.message_handler(state=PersonalData1.fullname)
async def answer_soha(message: Message, state: FSMContext):

    fullname = message.text
    await state.update_data(
        {
            'name': fullname
        }
    )
    await message.answer("Telefon raqamingizni kiriting:")
    await PersonalData1.next()

@dp.message_handler(state=PersonalData1.phoneNumber)
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
        <b>ism familiya sharifi</b>: {fullname}\n
        <b>Telefon raqamingiz</b>: {phone}
    """

    await comment(msg)
    

    await state.finish()
    await message.answer(msg, reply_markup=anketa1)

@dp.callback_query_handler(text="3ortga")
async def cancel_buying(call: CallbackQuery):
    await call.message.delete()
    photo = open("photos/tramplin.jpg", "rb")
    # habar = "<b>Tramplin IT Akademiyasi haqida qisqacha ma'lumot</b>\n\n"
    # habar += "Tramplin IT Akademiyasida siz Dasturlashni professionallardan o'rganishingiz mumkin.\n"
    # habar += "Kurs davomida yuqori malakali dasturchilardan maxsus metodika asosida sifatli ta'lim olishingiz va o'zlashtirgan bilimlaringizni amaliyotda 50 dan ortiq loyiha asosida o'z portfolioingizni yaratishingiz mumkin."
    await call.message.answer_photo(photo = photo, reply_markup=kurslarmenu)















