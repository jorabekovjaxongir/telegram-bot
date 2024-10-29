from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext
from utils.notify_admins import comment

from loader import dp
from states.yapon_takliflar import Yapon_PersonalData3
from keyboards.inline.yapon_menu import  yapon_menu, yapon_shikoyat_menu

@dp.callback_query_handler(text="yapon_shikoyat")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("提案や苦情を書いてください！")
    await Yapon_PersonalData3.yapon_text.set()

@dp.message_handler(state=Yapon_PersonalData3.yapon_text)
async def answer_soha(message: Message, state: FSMContext):
    text = message.text

    await state.update_data(
        {
            '提案と苦情': text
        }
    )
    await message.answer("電話番号を送信してください:")
    await Yapon_PersonalData3.yapon_phoneNumber.set()

@dp.message_handler(state=Yapon_PersonalData3.yapon_phoneNumber)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {
            'telefon_nomer': phone
        }
    )
    
    data = await state.get_data()
    txt = data.get('name')
    phone = data.get('telefon_nomer')



    msg = f"""
        以下の情報が届きました.\n
        すぐにオペレーターがご連絡させていただきます。\n\n\n
        <b>提案と苦情</b>: {txt}\n
        <b>あなたの電話番号</b>: {phone}
    """
    
    await comment(msg)
    
    await state.finish()
    # await state.reset_state(with_data=False)
    await message.answer(msg, reply_markup=yapon_shikoyat_menu)

@dp.callback_query_handler(text="1_戻る")
async def start(call: CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    await call.message.answer_photo(photo=photo,reply_markup=yapon_menu)
    await call.answer(cache_time=60)