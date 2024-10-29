import logging

from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from utils.notify_admins import comment


from loader import dp
from states.yapon_personalData import Yapon_PersonalData
from keyboards.inline.yapon_menu import  yapon_menu, yapon_informatsiya

@dp.callback_query_handler(text="yapon_vakansiya")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("どの方向で働きたいか:")
    await Yapon_PersonalData.yapon_qaysi_sohaga.set()

@dp.message_handler(state=Yapon_PersonalData.yapon_qaysi_sohaga)
async def answer_soha(message: Message, state: FSMContext):
    soha = message.text

    await state.update_data(
        {
            'フィールドが選択されています': soha
        }
    )
    await message.answer("フルネームを入力してください:")
    await Yapon_PersonalData.yapon_fullname.set()

@dp.message_handler(state=Yapon_PersonalData.yapon_fullname)
async def answer_fullname(message: Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {
            'F.I.O': fullname
        }
    )
    await message.answer("履歴書を次の宛先に提出してください。")
    await Yapon_PersonalData.next()

@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=Yapon_PersonalData.yapon_resume)
async def answer_resume(message: Message, state: FSMContext):
    resume = message.document

    await state.update_data(
        {
            '再開する': resume.file_name
        }
    )
    await message.answer("電話番号を送信してください:")
    await Yapon_PersonalData.next()

@dp.message_handler(state=Yapon_PersonalData.yapon_phoneNumber)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {
            '電話番号': phone
        }
    )
    
    data = await state.get_data()
    soha = data.get('フィールドが選択されています')
    fullname = data.get('F.I.O')
    resume = data.get('再開する')
    phone = data.get('電話番号')




    msg = (
        "以下の情報を受け取りました。\n"
        "オペレーターがすぐにご連絡いたします。\n\n\n"
        f"<b>提出した方向性</b>: {soha}\n"
        f"<b>名 姓</b>: {fullname}\n"
        f"<b>あなたの履歴書</b>: {resume}\n"
        f"<b>あなたの電話番号</b>: {phone}"
    )

    await comment(msg)
    
    await state.finish()
    await state.reset_state(with_data=False)
    await message.answer(msg, reply_markup=yapon_informatsiya)

@dp.callback_query_handler(text="yapon_2ortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    msg = "<b>Menyu:</b>"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=yapon_menu)
