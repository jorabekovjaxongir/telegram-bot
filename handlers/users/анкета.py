from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext
from utils.notify_admins import comment

from loader import dp
from states.rus_anketa import Rus_PersonalData1
from keyboards.inline.rus_menu import  курсыменю, анкета1

@dp.callback_query_handler(text="анкета")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ведите свое полное имя:")
    await Rus_PersonalData1.rus_fullname.set()

@dp.message_handler(state=Rus_PersonalData1.rus_fullname)
async def answer_soha(message: Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {
            'name': fullname
        }
    )
    await message.answer("Отправьте свой номер телефона:")
    await Rus_PersonalData1.rus_phoneNumber.set()

# @dp.message_handler(state=PersonalData.fullname)
# async def answer_fullname(message: Message, state: FSMContext):
#     fullname = message.text

#     await state.update_data(
#         {
#             'F.I.O': fullname
#         }
#     )
#     await message.answer("Telefon raqamingizni yuboring:")
#     await PersonalData.next()

@dp.message_handler(state=Rus_PersonalData1.rus_phoneNumber)
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
        Была получена следующая информация.\n
        Наши операторы свяжутся с вами в ближайшее время.\n\n\n
        <b>имя фамилия</b>: {fullname}\n
        <b>Ваш номер телефона</b>: {phone}
    """
    
    await comment(msg)
    
    await state.finish()
    # await state.reset_state(with_data=False)
    await message.answer(msg, reply_markup=анкета1)

@dp.callback_query_handler(text="3назад")
async def start(call: CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/kurslar.jpg",'rb')
    await call.message.answer_photo(photo=photo,reply_markup=курсыменю)
    await call.answer(cache_time=60)