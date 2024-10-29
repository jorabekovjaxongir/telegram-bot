
from aiogram import types
# from aiogram.dispatcher.filters import Command
# from aiogram.types import  ReplyKeyboardRemove
from keyboards.inline.tillar import tillar
from keyboards.inline.uzb_menuKeyboards import Menu, menu, sozlamalar_menu, aboutmenu, kurslarmenu, kurslar1, xodimlarmenu, otajon, rustam#, xusan, otabek,xurshid,miraziz

from loader import dp

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)

@dp.callback_query_handler(text="O'zbek")
async def menu_select(call: types.CallbackQuery):
    photo ="AgACAgIAAxkBAAIOR2cXwqAOMsnF5WgbwQ-3L6-OMjQ8AAI-5jEb9xrBSOfanVf2Yj1lAQADAgADeAADNgQ"
    habar = "<b>Tramplin IT Akademiyasi haqida qisqacha ma'lumot:</b>\n\n"
    habar += "Tramplin IT Akademiyasida siz Dasturlashni professionallardan o'rganishingiz mumkin.\n"
    habar += "Kurs davomida yuqori malakali dasturchilardan maxsus metodika asosida sifatli ta’lim olishingiz va o'zlashtirgan bilimlaringizni amaliyotda 50 dan ortiq loyiha asosida o'z portfolioingizni yaratishingiz mumkin."
    await call.message.delete()
    await call.message.answer_photo(photo=photo, caption=habar, reply_markup=Menu)

@dp.callback_query_handler(text="sozlamalar")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = "AgACAgIAAxkBAAIT2WcdLMpyUGjBZzDKSU4qAmFVCtUNAALK6DEb0FXxSB6SXKAQwlDMAQADAgADeQADNgQ"
    # msg = f"""
    # Assalomu alleykum hurmatli <b>{call.message.from_user.username}👨🏻‍💻</b>!\n<b>Tramplin</b>ga.\nXush kelibsiz🤝\n\nЗдравствуйте Уважаемый <b>{call.message.from_user.username}👨🏻‍💻</b>!\nДобро пожаловать на <b>Трамплин</b>\n\n<b>Tillni tanlang👇\nВыберите язык👇</b>
    # """
    await call.message.answer_photo(photo=photo,reply_markup=sozlamalar_menu)

@dp.callback_query_handler(text="Tillar")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = "AgACAgIAAxkBAAITxWcdKMOJ7WyS0528mIk5t2zVmz_iAAIw5zEbhD7pSAiZ4O9hO6AqAQADAgADeQADNgQ"
    await call.message.answer_photo(photo=photo,reply_markup=tillar)

# @dp.callback_query_handler(text="sozlamalarortga")
# async def menu_handler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = "AgACAgIAAxkBAAIT3WcdMAziUFS9YGm1ik2S4GiqTTRlAALb6DEb0FXxSMjl6tUmDzgaAQADAgADeQADNgQ"
#     await call.message.answer_photo(photo=photo,reply_markup=menu)

@dp.callback_query_handler(text="Menu")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = open("photos/about.jpg", 'rb')
    await call.message.answer_photo(photo=photo, reply_markup=menu)
    # await call.message.answer("O'zbek til tanlandi:",reply_markup=ReplyKeyboardRemove())


@dp.callback_query_handler(text="menuortga")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/tramplin.jpg",'rb')
    msg = f"""
    Assalomu alleykum hurmatli <b>{call.message.from_user.username}👨🏻‍💻</b>!\n<b>Tramplin</b>ga.\nXush kelibsiz🤝\n\nЗдравствуйте Уважаемый <b>{call.message.from_user.username}👨🏻‍💻</b>!\nДобро пожаловать на <b>Трамплин</b>\n\n<b>Tillni tanlang👇\nВыберите язык👇</b>
    """
    await call.message.answer_photo(photo=photo,caption=msg,reply_markup=tillar)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="about")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/tramplin2.jpg",'rb')
    msg = "<b>TRAMPLIN IT AKADEMIYASI ZAMONAVIY KASBLARDAN BIR BO'LGAN DASTURLASH SOHASINING TURLI YO'NALISHLARIDA AMALIYOTGA ASOSLANGAN METODIKA ASOSIDA O'QUVCHILARGA TA'LIM BERADI.</b>"
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=aboutmenu)


@dp.callback_query_handler(text="aboutortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    # msg = "<b>Menyu:</b>"
    await call.message.answer_photo(photo=photo, reply_markup=menu)

@dp.callback_query_handler(text="kurslar")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/kurslar.jpg",'rb')
    await call.message.answer_photo(photo=photo,reply_markup=kurslarmenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="kurslarortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    # msg = "<b>Menyu:</b>"
    await call.message.answer_photo(photo=photo, reply_markup=menu)



@dp.callback_query_handler(text="frontend")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAIOJWcXiHuK1bV992KkXKPV3nmGc97DAAJLWwAC9xq5SNJxJjHvcKwKNgQ"
    msg = "<b>Frontend dasturlash kursidan dars jarayonlari:</b>\n\n"
    msg += "🧑‍💻 Kursda o'quvchilarimiz, darsda o'rgangan bilimlarini amaliyotda qo'llab ko'rishmoqda, bu orqali ular o'rgangan bilimlarini yanada mustahkamlashadi.\n\n"
    msg += "Har bir darsda nazariy va amaliy mashg'ulotlar birgalikda olib borilib, talabalar real loyihalar ustida ishlash imkoniyatiga ega bo'lishadi. Shu tariqa ular nafaqat kod yozishni, balki mijozlar ehtiyojlarini tushunib, ularga mos dasturlarni  yaratishni o'rganishadi."
    await call.message.answer_video(video=video, caption=msg,reply_markup=kurslar1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="ortga2")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/kurslar.jpg",'rb')
    await call.message.answer_photo(photo=photo,reply_markup=kurslarmenu)

@dp.callback_query_handler(text="backend")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAIOJ2cXiO1rUutqhxmj6tvsFiWlJ5htAAJQWwAC9xq5SDqZddgsbTYjNgQ"
    msg = "<b>Backend Python kursi dars jarayonlaridan lavha:</b>\n\n"
    msg +="Backend kursimiz amaliyotga asoslangan bo'lib, o'quvchilar darslar davomida o'rgangan narsalarini, amaliy qo'llab ko'rishadi.\n\n"
    msg +="🧑‍💻Kurs yakuniga o'quvchilarimizda real loyiha va tayyor portfolio bo'ladi. Yaxshi o'qigan va imtihondan o'ta olgan o'quvchilarimizga sertifikat ham taqdim etiladi."
    await call.message.answer_video(video=video, caption=msg,reply_markup=kurslar1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="kibr")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAIOK2cXirgMP-iF6IpMJ_6dNv1QXAvgAAJlWwAC9xq5SOkNi7gcNNTwNgQ"
    msg ="<b>Kiberxavfsizlik:</b>\n\n"
    msg += "<b>Kiberxavfsizlik</b> kompyuter tizimlari, tarmoqlari, dasturlarga  ruxsatsiz kirish, kiberhujumlardan himoya qilish amaliyotini anglatadi. \n\n"
    msg += "<b>🔹 XXI asr</b> raqamli axborot texnologiyalari rivojlangani sari Kiberxavfsizlikning ahamiyati sezilarli darajada oshdi, chunki kundalik hayotimiz, biznesimiz va ish faoliyatmiz raqamli axborot bilan uzviy bog’langan. Shunday ekan bu soha vakillariga talab kundan kunga ortib bormoqda."
    await call.message.answer_video(video=video, caption=msg,reply_markup=kurslar1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="grafik")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAIOKWcXiQI9lwvrqUE7ERh1atjodcpPAAJRWwAC9xq5SEB2ZxoDAuNINgQ"
    msg = "<b>Grafik dizayn kursimizda nimalarni o'rganasiz?:</b>\n\n"
    msg += "Oddiy va sodda tilda 0 dan boshlab vizual kontent yaratishni o'rganasiz. Bu kursda nazariy bilimlarni amaliy mashg'ulotlar bilan mustahkamlaysiz.\n\n"
    msg += "Dizaynning asosiy tamoyillaridan tortib, zamonaviy grafik vositalar va dasturlarda ishlashgacha bo'lgan jarayonlarni chuqur o‘rganasiz.\n\n"
    msg += "Kursimiz sizni professional grafik dizayner bo'lishingizga tayyorlaydi!"
    await call.message.answer_video(video=video, caption=msg, reply_markup=kurslar1)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="xodimlar")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=xodimlarmenu)
    # await call.answer(cache_time=60)

@dp.callback_query_handler(text="xodimlarortga")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    # msg = "<b>Menyu:</b>"
    await call.message.answer_photo(photo=photo, reply_markup=menu)

@dp.callback_query_handler(text="otajon")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/otajon.jpg",'rb')
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Otajon Bozorboyev.\n\n"   
    msg += "<b>Tug'ilgan yili va joyi: \n</b>"
    msg += "8-yanvar 1999-yil;\n"
    msg += "Jizzax viloyati, Jizzax shahri.\n\n"
    msg += "<b>Ta'limi: \n</b>"
    msg += "Toshkent temir yo'l transport kasb-hunar kolleji Buxgalteriya hisobi va audit (2015-2018).\n\n"
    msg += "<b>Ish tajribasi: \n</b>"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi ish o'rganuvchisi (2018-2019);\n"
    msg += "Jizzax temir yo'l masofasi xodimlar bo'limi nazoratchisi (2019-2023);\n"
    msg += "Astro Education o'quv markazi dasturlash kursi mentori (2023-hozirgacha).\n\n"
    msg += "<b>Texnik ko'nikmalari: \n</b>"
    msg += "C, Python, Django, Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot, Adobe Photoshop, Web Scraping, Parsing, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)\n\n"
    msg += "<b>Tillar: \n</b>"
    msg += "O'zbek tili (Ona tili);\n"
    msg += "Ingliz tili (B2);\n"
    msg += "Arab tili (O'qiy olish)."
    await call.message.answer_photo(photo=photo,caption=msg,reply_markup=otajon)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="otajonortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=xodimlarmenu)

@dp.callback_query_handler(text="rustamjon")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/tramplin.jpg",'rb')
    msg = "<b>Ismi-sharifi: </b>\n"
    msg += "Isroilov Rustamjon.\n\n"   
    msg += "<b>Tug'ilgan yili va joyi: \n</b>"
    msg += "2-dekabr 2002-yil;\n"
    msg += "Farg'ona viloyati, Qo'qon shahri.\n\n"
    msg += "<b>Ta'limi: </b>\n"
    msg += "Muhammad al-Xorazmiy nomidagi Toshkent Axborot Texnologiyalari Universiteti(TATU) (2021….).\n\n"
    msg += "<b>Ish tajribasi: </b>\n"
    msg += "Isystem IT academy Foundation Mentor(2022-yildan hozirga qadar);\n"
    msg += "Astro Education Python Beckend Mentor(2023-yildan hozirga qadar);\n\n"
    msg += "<b>Texnik ko'nikmalari: \n</b>"
    msg += "C++, Python, Django, Django Rest, SQLite, PostgreSQL, Git, GitHub, HTML, CSS, Telegram Bot, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)\n\n"
    msg += "<b>Tillar: \n</b>"
    msg += "O'zbek tili (Ona tili);\n"
    msg += "Ingliz tili (Tushuna olaman);\n"
    await call.message.answer_photo(photo=photo,caption=msg,reply_markup=rustam)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="rustamortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Xodimlar👇</b>", reply_markup=xodimlarmenu)

