from aiogram import types
from aiogram.types import  ReplyKeyboardRemove
from keyboards.inline.tillar import tillar
from keyboards.inline.rus_menu import Меню, меню,rus_sozlamalar_menu, абоутменю, курсыменю, курсы1, сотрудникименю, отажон, рустам#, xusan, otabek,xurshid,miraziz

from loader import dp

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)

@dp.callback_query_handler(text="Русский")
async def menu_select(call: types.CallbackQuery):
    await call.message.delete()
    # await message.answer("Был выбран Русский язык.",reply_markup=ReplyKeyboardRemove())
    photo ="AgACAgIAAxkBAAIOR2cXwqAOMsnF5WgbwQ-3L6-OMjQ8AAI-5jEb9xrBSOfanVf2Yj1lAQADAgADeAADNgQ"
    habar = "<b>Краткая информация об Трамплин IT Академии:</b>\n\n"
    habar += "Трамплин IT Aкадемии вы можете изучать программирование у профессионалов.\n"
    habar += "В ходе курса вы сможете пройти качественное обучение у высококвалифицированных программистов по специальной методике и создать собственное портфолио на основе более чем 50 проектов, используя полученные знания."
    await call.message.answer_photo(photo=photo, caption=habar, reply_markup=Меню)

# @dp.callback_query_handler(text="1назад")
# async def menu_handler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = open("photos/tramplin.jpg",'rb')
#     msg = f"""
#     Assalomu alleykum hurmatli <b>{call.message.from_user.username}👨🏻‍💻</b>!\n<b>Tramplin</b>ga.\nXush kelibsiz🤝\n\nЗдравствуйте Уважаемый <b>{call.message.from_user.username}👨🏻‍💻</b>!\nДобро пожаловать на <b>Трамплин</b>\n\n<b>Tillni tanlang👇\nВыберите язык👇</b>
#     """
#     await call.message.answer_photo(photo=photo, caption=msg, reply_markup=tillar)
@dp.callback_query_handler(text="rus_Tillar")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = "AgACAgIAAxkBAAITxWcdKMOJ7WyS0528mIk5t2zVmz_iAAIw5zEbhD7pSAiZ4O9hO6AqAQADAgADeQADNgQ"
    await call.message.answer_photo(photo=photo,reply_markup=tillar)

@dp.callback_query_handler(text="rus_sozlamalar")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = "AgACAgIAAxkBAAIT2WcdLMpyUGjBZzDKSU4qAmFVCtUNAALK6DEb0FXxSB6SXKAQwlDMAQADAgADeQADNgQ"
    # msg = f"""
    # Assalomu alleykum hurmatli <b>{call.message.from_user.username}👨🏻‍💻</b>!\n<b>Tramplin</b>ga.\nXush kelibsiz🤝\n\nЗдравствуйте Уважаемый <b>{call.message.from_user.username}👨🏻‍💻</b>!\nДобро пожаловать на <b>Трамплин</b>\n\n<b>Tillni tanlang👇\nВыберите язык👇</b>
    # """
    await call.message.answer_photo(photo=photo,reply_markup=rus_sozlamalar_menu)

# @dp.callback_query_handler(text="rus_sozlamalarortga")
# async def menu_handler(call: types.CallbackQuery):
#     await call.message.delete()
#     photo = "AgACAgIAAxkBAAIT3WcdMAziUFS9YGm1ik2S4GiqTTRlAALb6DEb0FXxSMjl6tUmDzgaAQADAgADeQADNgQ"
#     await call.message.answer_photo(photo=photo,reply_markup=меню)

@dp.callback_query_handler(text="Mеню")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg", 'rb')
    msg = "<b>Меню:</b>"
    await call.message.answer_photo(photo=photo,caption=msg,reply_markup=меню)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="менуназад")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/tramplin.jpg",'rb')
    msg = f"""
    Assalomu alleykum hurmatli <b>{call.message.from_user.username}👨🏻‍💻</b>!\n<b>Tramplin</b>ga.\nXush kelibsiz🤝\n\nЗдравствуйте Уважаемый <b>{call.message.from_user.username}👨🏻‍💻</b>!\nДобро пожаловать на <b>Трамплин</b>\n\n<b>Tillni tanlang👇\nВыберите язык👇</b>
    """
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=tillar)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="онас")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/tramplin2.jpg",'rb')
    msg = "<b>В Академии Tрамплин подготовка студентов по различным направлениям программирования, одной из современных профессий, на основе методолгии, основанной на практике.</b>"
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=абоутменю)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="абоутназад")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    msg = "<b>Меню:</b>"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=меню)

@dp.callback_query_handler(text="Курсы")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/kurslar.jpg",'rb')
    await call.message.answer_photo(photo=photo,reply_markup=курсыменю)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="курсыназад")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    msg = "<b>Меню:</b>"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=меню)

@dp.callback_query_handler(text="Фронтентд")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAIOJWcXiHuK1bV992KkXKPV3nmGc97DAAJLWwAC9xq5SNJxJjHvcKwKNgQ"
    msg = "<b>Уроки курса Фронтенд программирование:</b>\n\n"
    msg += "🧑‍💻 В ходе курса наши студенты используют полученные на уроке знания на практике, благодаря чему они еще больше закрепят полученные знания..\n\n"
    msg += "На каждом уроке теоретические и практические занятия проводятся совместно, а студенты имеют возможность работать над реальными проектами. Таким образом они учатся не только писать код, но и понимать потребности клиентов и создавать подходящие им программы."
    await call.message.answer_video(video=video, caption=msg,reply_markup=курсы1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="назад2")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/kurslar.jpg",'rb')
    await call.message.answer_photo(photo=photo,reply_markup=курсыменю)

@dp.callback_query_handler(text="бекенд")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAIOJ2cXiO1rUutqhxmj6tvsFiWlJ5htAAJQWwAC9xq5SDqZddgsbTYjNgQ"
    msg = "<b>Уроки курса Бекенд программирование:</b>\n\n"
    msg +="Наш серверный курс основан на практике, и студенты получают практический опыт применения того, чему они научились во время занятий.\n\n"
    msg +="🧑‍💻На каждом уроке теоретические и практические занятия проводятся совместно, а студенты имеют возможность работать над реальными проектами. Таким образом они учатся не только писать код, но и понимать потребности клиентов и создавать подходящие им программы."
    await call.message.answer_video(video=video, caption=msg,reply_markup=курсы1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Кибербезопасность")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAIOK2cXirgMP-iF6IpMJ_6dNv1QXAvgAAJlWwAC9xq5SOkNi7gcNNTwNgQ"
    msg ="<b>Кибербезопасность:</b>\n\n"
    msg += "<b>Кибербезопасность:</b> относится к практике защиты от несанкционированного доступа к компьютерным системам, сетям, программам и кибератакам. \n\n"
    msg += "<b>🔹 XXI век</b> с развитием цифровых информационных технологий значимость Кибербезопасности значительно возросла, ведь наша повседневная жизнь, бизнес и трудовая деятельность неразрывно связаны с цифровой информацией. Поэтому спрос на представителей этой сферы растет с каждым днем."
    await call.message.answer_video(video=video, caption=msg,reply_markup=курсы1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Графический_дизайн")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAIOKWcXiQI9lwvrqUE7ERh1atjodcpPAAJRWwAC9xq5SEB2ZxoDAuNINgQ"
    msg = "<b>Чему вы научитесь на нашем курсе графического дизайна?:</b>\n\n"
    msg += "Вы научитесь создавать визуальный контент с нуля простым и понятным языком. На этом курсе вы укрепите теоретические знания практическими упражнениями.\n\n"
    msg += "Вы подробно изучите процессы: от основных принципов дизайна до работы с современными графическими инструментами и программным обеспечением.\n\n"
    msg += "Наш курс готовит вас стать профессиональным графическим дизайнером!"
    await call.message.answer_video(video=video, caption=msg, reply_markup=курсы1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="Сотрудники")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    # msg = "yuqori malakali dasturchilardan maxsus metodika asosida sifatli ta’lim olishingiz"
    await call.message.answer(f"<b>Сотрудники👇</b>", reply_markup=сотрудникименю)

@dp.callback_query_handler(text="сотрудникиназад")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    msg = "<b>Меню:</b>"
    await call.message.answer_photo(photo=photo,caption=msg, reply_markup=меню)

@dp.callback_query_handler(text="Отажон_Базарбаев")
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
    await call.message.answer_photo(photo=photo,caption=msg,reply_markup=отажон)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="отажонназад")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Сотрудники👇</b>", reply_markup=сотрудникименю)

@dp.callback_query_handler(text="Исраилов_Рустам")
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
    await call.message.answer_photo(photo=photo,caption=msg,reply_markup=рустам)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="рустамназад")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>Сотрудники👇</b>", reply_markup=сотрудникименю)







