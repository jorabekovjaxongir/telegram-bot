
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext
from utils.notify_admins import comment


from loader import dp
from states.yapon_anketa import Yapon_PersonalData1
from keyboards.inline.yapon_menu import  yapon_kurslarmenu, yapon_anketa1

@dp.callback_query_handler(text="yapon_anketa")
async def enter_text(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("フルネームを入力してください")
    await Yapon_PersonalData1.yapon_fullname.set()

@dp.message_handler(state=Yapon_PersonalData1.yapon_fullname)
async def answer_soha(message: Message, state: FSMContext):

    fullname = message.text
    await state.update_data(
        {
            '名前': fullname
        }
    )
    await message.answer("電話番号を入力してください:")
    await Yapon_PersonalData1.next()

@dp.message_handler(state=Yapon_PersonalData1.yapon_phoneNumber)
async def answer_phone(message: Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {
            '電話番号': phone
        }
    )
    
    data = await state.get_data()
    fullname = data.get('名前')
    phone = data.get('電話番号')

    await message.answer("このアカウントは完全に登録されています。\n\n登録されたアカウント情報は以下のとおりです。")


    msg = f"""
        以下の情報を受け取りました。\n
        オペレーターがすぐにご連絡いたします。\n\n\n
        <b>名 姓</b>: {fullname}\n
        <b>あなたの電話番号</b>: {phone}
    """

    await comment(msg)

    await state.finish()
    await message.answer(msg, reply_markup=yapon_anketa1)

@dp.callback_query_handler(text="yapon_3ortga")
async def cancel_buying(call: CallbackQuery):
    await call.message.delete()
    photo = open("photos/tramplin.jpg", "rb")
    habar = "<b>Springboard IT Academy に関する概要情報</b>\n\n"
    habar += "Springboard IT Academyではプロからプログラミングを学ぶことができます。\n"
    habar += "コース中は、特別な方法論に基づいた高度な資格を持つプログラマーから質の高い教育を受け、実際に行われた 50 以上のプロジェクトに基づいて独自のポートフォリオを作成できます。"
    await call.message.answer_photo(photo = photo, caption=habar, reply_markup=yapon_kurslarmenu)

