
from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp
from states.ru_personaldat import ru_personalData
from keyboards.inline.rus_menu import  меню, информатсия

@dp.callback_query_handler(text="Вакансия")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("В каком направлении вы хотите работать:")
    await ru_personalData.ru_qaysi_sohaga.set()

@dp.message_handler(state=ru_personalData.ru_qaysi_sohaga)
async def answer_soha(message: Message, state: FSMContext):
    soha = message.text

    await state.update_data(
        {
            'поле выбрано': soha
        }
    )
    await message.answer("Введите свое полное имя:")
    await ru_personalData.ru_fullname.set()

@dp.message_handler(state=ru_personalData.ru_fullname)
async def answer_fullname(message: Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {
            'Ф.И.О.': fullname
        }
    )
    await message.answer("Отправьте свое резюме по адресу:")
    await ru_personalData.next()

@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=ru_personalData.ru_resume)
async def answer_resume(message: Message, state: FSMContext):
    резюме = message.document

    await state.update_data(
        {
            'резюме': резюме.file_name
        }
    )
    await message.answer("Отправьте свой номер телефона:")
    await ru_personalData.next()

@dp.message_handler(state=ru_personalData.ru_phoneNumber)
async def answer_phone(message: Message, state: FSMContext):
    номер_телефона = message.text

    await state.update_data(
        {
            'номер телефона': номер_телефона
        }
    )
    
    data = await state.get_data()
    soha = data.get('поле выбрано')
    полное_имя = data.get('Ф.И.О.')
    резюме = data.get('резюме')
    номер_телефона = data.get('номер телефона')

    msg = (
        "Была получена следующая информация.\n"
        "Наши операторы свяжутся с вами в ближайшее время.\n\n\n"
        f"<b>Направление, которое вы отправили</b>: {soha}\n"
        f"<b>имя фамилия</b>: {полное_имя}\n"
        f"<b>Ваше резюме</b>: {резюме}\n"
        f"<b>Ваш номер телефона</b>: {номер_телефона}"
    )

    
    await state.finish()
    await message.answer(msg, reply_markup=информатсия)

@dp.callback_query_handler(text="2назад")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    msg = "<b>Меню:</b>"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=меню)


# import logging

# from aiogram import types
# from aiogram.types import Message, CallbackQuery
# from aiogram.dispatcher import FSMContext

# from loader import dp
# from states.ru_personaldat import ru_personalData
# from keyboards.inline.rus_menu import ru_informatsiya

# @dp.callback_query_handler(text="ru_vakansiya")
# async def enter_text(call: CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("В каком направлении вы хотите работать:")
#     await ru_personalData.ru_qaysi_sohaga.set()

# @dp.message_handler(state=ru_personalData.ru_qaysi_sohaga)
# async def answer_soha(message: Message, state: FSMContext):
#     ru_soha = message.text

#     await state.update_data(
#         {
#             'поле выбрано': ru_soha
#         }
#     )
#     await message.answer("Введите свое полное имя:")
#     await ru_personalData.ru_fullname.set()

# @dp.message_handler(state=ru_personalData.ru_fullname)
# async def answer_fullname(message: Message, state: FSMContext):
#     ru_fullname = message.text

#     await state.update_data(
#         {
#             'Ф.И.О.': ru_fullname
#         }
#     )
#     await message.answer("Отправьте свое резюме по адресу:")
#     await ru_personalData.next()

# @dp.message_handler(content_types=types.ContentType.DOCUMENT, state=ru_personalData.ru_resume)
# async def answer_resume(message: Message, state: FSMContext):
#     ru_resume = message.document

#     await state.update_data(
#         {
#             'резюме': ru_resume.file_name
#         }
#     )
#     await message.answer("Отправьте свой номер телефона:")
#     await ru_personalData.next()

# @dp.message_handler(state=ru_personalData.ru_phoneNumber)
# async def answer_phone(message: Message, state: FSMContext):
#     ru_phone = message.text

#     await state.update_data(
#         {
#             'номер телефона': ru_phone
#         }
#     )
    
#     data = await state.get_data()
#     ru_soha = data.get('поле выбрано')
#     ru_fullname = data.get('Ф.И.О.')
#     ru_resume = data.get('резюме')
#     ru_phone = data.get('номер телефона')

#     ru_msg = (
#         "<b>Была получена следующая информация.</b>\n"
#         "<b>Наши операторы свяжутся с вами в ближайшее время.</b>\n\n\n"
#         f"<b>Направление, которое вы отправили</b>: {ru_soha}\n"
#         f"<b>имя фамилия</b>: {ru_fullname}\n"
#         f"<b>Ваше резюме</b>: {ru_resume}\n"
#         f"<b>Ваш номер телефона</b>: {ru_phone}"
#     )

    
#     await message.answer(ru_msg, reply_markup=ru_informatsiya)
#     await state.finish()
#     await state.reset_state(with_data=False)