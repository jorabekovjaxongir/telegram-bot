from aiogram import types
from aiogram.types import  ReplyKeyboardRemove
from keyboards.inline.tillar import tillar
from keyboards.inline.yapon_menu import yapon_Menu, yapon_menu,yapon_sozlamalar_menu, yapon_aboutmenu, yapon_kurslarmenu, yapon_kurslar1, yapon_xodimlarmenu, yapon_otajon, yapon_rustam

from loader import dp

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)

@dp.callback_query_handler(text="Yaponiya")
async def menu_select(call: types.CallbackQuery):
    await call.message.delete()
    # await message.answer("Был выбран Русский язык.",reply_markup=ReplyKeyboardRemove())
    photo ="AgACAgIAAxkBAAIOR2cXwqAOMsnF5WgbwQ-3L6-OMjQ8AAI-5jEb9xrBSOfanVf2Yj1lAQADAgADeAADNgQ"
    habar = "<b>Springboard IT Academy についての簡単な情報:</b>\n\n"
    habar += "プロからプログラミングを学べるITアカデミーの踏み台。\n"
    habar += "コース中には、特別な方法論を使用した高度な資格を持つプログラマーから質の高いトレーニングを受け、得た知識を使用して 50 以上のプロジェクトに基づいて独自のポートフォリオを作成することができます。"
    await call.message.answer_photo(photo=photo, caption=habar, reply_markup=yapon_Menu)

@dp.callback_query_handler(text="yapon_Tillar")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = "AgACAgIAAxkBAAITxWcdKMOJ7WyS0528mIk5t2zVmz_iAAIw5zEbhD7pSAiZ4O9hO6AqAQADAgADeQADNgQ"
    await call.message.answer_photo(photo=photo,reply_markup=tillar)

@dp.callback_query_handler(text="yapon_sozlamalar")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    photo = "AgACAgIAAxkBAAIT2WcdLMpyUGjBZzDKSU4qAmFVCtUNAALK6DEb0FXxSB6SXKAQwlDMAQADAgADeQADNgQ"
    # msg = f"""
    # Assalomu alleykum hurmatli <b>{call.message.from_user.username}👨🏻‍💻</b>!\n<b>Tramplin</b>ga.\nXush kelibsiz🤝\n\nЗдравствуйте Уважаемый <b>{call.message.from_user.username}👨🏻‍💻</b>!\nДобро пожаловать на <b>Трамплин</b>\n\n<b>Tillni tanlang👇\nВыберите язык👇</b>
    # """
    await call.message.answer_photo(photo=photo,reply_markup=yapon_sozlamalar_menu)

@dp.callback_query_handler(text="yapon_Menu")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg", 'rb')
    await call.message.answer_photo(photo=photo,reply_markup=yapon_menu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="yapon_about")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/tramplin2.jpg",'rb')
    msg = "<b>Springboard Academy では、学生は実践ベースの方法論に基づいて、現代の職業の 1 つであるプログラミングのさまざまな分野のトレーニングを受けます。</b>"
    await call.message.answer_photo(photo=photo, caption=msg, reply_markup=yapon_aboutmenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="yapon_aboutortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    await call.message.answer_photo(photo=photo, reply_markup=yapon_menu)

@dp.callback_query_handler(text="yapon_kurslar")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/kurslar.jpg",'rb')
    await call.message.answer_photo(photo=photo,reply_markup=yapon_kurslarmenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="yapon_kurslarortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    await call.message.answer_photo(photo=photo, reply_markup=yapon_menu)

@dp.callback_query_handler(text="yapon_frontend")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAIOJWcXiHuK1bV992KkXKPV3nmGc97DAAJLWwAC9xq5SNJxJjHvcKwKNgQ"
    msg = "<b>フロントエンド プログラミング コースからの教訓:</b>\n\n"
    msg += "🧑‍💻 コース中、学生は授業で得た知識を実際に使用し、これにより得た知識をさらに定着させます。\n\n"
    msg += "各レッスンでは、理論的授業と実践的授業が同時に行われ、学生は実際のプロジェクトに取り組む機会があります。このようにして、彼らはコードを書くだけでなく、クライアントのニーズを理解し、それに適したプログラムを作成することも学びます。"
    await call.message.answer_video(video=video, caption=msg,reply_markup=yapon_kurslar1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="yapon_ortga2")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/kurslar.jpg",'rb')
    await call.message.answer_photo(photo=photo,reply_markup=yapon_kurslarmenu)

@dp.callback_query_handler(text="yapon_backend")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAIOJ2cXiO1rUutqhxmj6tvsFiWlJ5htAAJQWwAC9xq5SDqZddgsbTYjNgQ"
    msg = "<b>バックエンド プログラミング コースのレッスン:</b>\n\n"
    msg +="私たちのサーバーコースは実践的なもので、学生はクラス中に学んだことを実践的に応用することができます。\n\n"
    msg +="🧑‍💻各レッスンでは、理論的授業と実践的授業が一緒に行われ、学生は実際のプロジェクトに取り組む機会があります。このようにして、彼らはコードを書くだけでなく、クライアントのニーズを理解し、それに適したプログラムを作成することも学びます。"
    await call.message.answer_video(video=video, caption=msg,reply_markup=yapon_kurslar1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="yapon_kibr")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAIOK2cXirgMP-iF6IpMJ_6dNv1QXAvgAAJlWwAC9xq5SOkNi7gcNNTwNgQ"
    msg ="<b>サイバーセキュリティ:</b>\n\n"
    msg += "<b>サイバーセキュリティ:</b> コンピュータ システム、ネットワーク、プログラムへの不正アクセス、およびサイバー攻撃から保護する実践を指します。 \n\n"
    msg += "<b>🔹 21世紀</b> デジタル情報技術の発展に伴い、私たちの日常生活、ビジネス、仕事活動がデジタル情報と密接に結びついているため、サイバーセキュリティの重要性が大幅に高まっています。したがって、この分野の代表者に対する需要は日々高まっています。"
    await call.message.answer_video(video=video, caption=msg,reply_markup=yapon_kurslar1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="yapon_grafik")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    video = "BAACAgIAAxkBAAIOKWcXiQI9lwvrqUE7ERh1atjodcpPAAJRWwAC9xq5SEB2ZxoDAuNINgQ"
    msg = "<b>グラフィック デザイン コースでは何を学びますか?:</b>\n\n"
    msg += "シンプルでわかりやすい言語でビジュアルコンテンツをゼロから作成する方法を学びます。このコースでは、実践的な演習を通じて理論的知識を強化します。\n\n"
    msg += "基本的なデザイン原則から最新のグラフィック ツールやソフトウェアの使用に至るまで、プロセスを詳細に学習します。\n\n"
    msg += "私たちのコースは、プロのグラフィックデザイナーになるための準備を整えます。"
    await call.message.answer_video(video=video, caption=msg, reply_markup=yapon_kurslar1)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="yapon_xodimlar")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    # msg = "yuqori malakali dasturchilardan maxsus metodika asosida sifatli ta’lim olishingiz"
    await call.message.answer(f"<b>従業員👇</b>", reply_markup=yapon_xodimlarmenu)

@dp.callback_query_handler(text="yapon_xodimlarortga")
async def menu_handler(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/about.jpg",'rb')
    await call.message.answer_photo(photo=photo, reply_markup=yapon_menu)

@dp.callback_query_handler(text="yapon_otajon")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    photo = open("photos/otajon.jpg",'rb')
    msg = "<b>イスミ・シャリフス: </b>\n"
    msg += "オタゾン・ボゾルボエフ。\n\n"   
    msg += "<b>トゥギルガンまたはヴァ・エイ: \n</b>"
    msg += "1999 年 1 月 8 日。\n"
    msg += "ジザフ・ヴィロヤティ、ジザフ・シャクリ。\n\n"
    msg += "<b>タリミ: \n</b>"
    msg += "トシケント・テミル・エル・トランスポート・カスブ・フナール大学会計監査（2015-2018）。\n\n"
    msg += "<b>イシュ・タズリバシ: \n</b>"
    msg += "ジザフ・テミル・エル・マソフィアス・ホディムラー・ボリミ・イッシュ・オルガノフキス（2018-2019）。\n"
    msg += "ジザフ・テミル・エル・マソフィヤス・ホディムラル・ボリミ・ナゾラチシ（2019-2023）。\n"
    msg += "Astro Education okov markazi dasturlash コースのメンター (2023-khozirgaha)。\n\n"
    msg += "<b>コニクタラリ技術者: \n</b>"
    msg += "C, Python, Django, Django Rest, SQLite, PostgreSQL, MySQL, Git, GitHub, HTML, CSS, Telegram Bot, Adobe Photoshop, Web Scraping, Parsing, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)\n\n"
    msg += "<b>言語: \n</b>"
    msg += "ウズベク語(母国語);\n"
    msg += "英語(B2);\n"
    msg += "アラビア語 (読み)。"
    await call.message.answer_photo(photo=photo,caption=msg,reply_markup=yapon_otajon)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="yapon_otajonortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>従業員👇</b>", reply_markup=yapon_xodimlarmenu)

@dp.callback_query_handler(text="yapon_rustamjon")
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
    await call.message.answer_photo(photo=photo,caption=msg,reply_markup=yapon_rustam)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="yapon_rustamortga")
async def start(call: types.CallbackQuery):
    await call.message.delete()
    users = {call.from_user.id:call.from_user.username}
    await call.message.answer(f"<b>従業員👇</b>", reply_markup=yapon_xodimlarmenu)
