from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup 


Меню = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌎 Mеню", callback_data="Mеню"),
            # InlineKeyboardButton(text="⬅️ Назад", callback_data="1назад"),
        ],
    ],row_width=True
)

меню = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📜 О нас", callback_data="онас"),
            InlineKeyboardButton(text="📊 Курсы", callback_data="Курсы"),
        ],
        [
            InlineKeyboardButton(text="👨‍💻 Сотрудники", callback_data="Сотрудники"),
            InlineKeyboardButton(text="🧾 Вакансия", callback_data="Вакансия"),
        ],
        [
            InlineKeyboardButton(text="🛠 Настройки", callback_data="rus_sozlamalar"),
        ],
        # [
            # InlineKeyboardButton(text="📞 Связаться с нами", url="https://t.me/tramplin_uz" ),
        #     InlineKeyboardButton(text="⬅️ Назад", callback_data="менуназад"),
        # ],
    ],row_width=True
)

# rus_shikoyat = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="",callback_data="rus_shikoyatortga")
#         ]
#     ]
# )

rus_sozlamalar_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🗣️ Языки", callback_data="rus_Tillar" ),
            InlineKeyboardButton(text="📣 Жалобы и предложения", callback_data="rus_shikoyat"),
        ],
    ],row_width=True
)

rus_shikoyat_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Назад",callback_data="1_жалобе")
        ],
    ],
)

абоутменю = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🎦 Видео", url="https://youtube.com/shorts/qsHai1S7wKg?si=GnAz1KR9ukhCDiNB"),
            InlineKeyboardButton(text="⬅️ Назад", callback_data="абоутназад"),
        ],
    ],row_width=True
)

курсыменю =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📘 Фронтентд",callback_data="Фронтентд"),
            InlineKeyboardButton(text="📕 Серверная часть", callback_data="бекенд"),
        ],
        [
            InlineKeyboardButton(text="📙 Кибербезопасность",callback_data="Кибербезопасность"),
            InlineKeyboardButton(text="📗 Графический дизайн",callback_data="Графический_дизайн"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="курсыназад"),
        ],
    ],row_width=True
)

информатсия = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="⤴️ Назад", callback_data='2назад')
        ]
    ]
)

анкета1 = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="⤴️ Назад", callback_data='3назад')
        ]
    ]
)

курсы1= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✍️ Запись на курсы", callback_data="анкета"),
            InlineKeyboardButton(text="⬅️ Назад", callback_data="назад2"),
        ],
    ],)


сотрудникименю = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👤 Отажон Базарбаев", callback_data="Отажон_Базарбаев"),
            InlineKeyboardButton(text="👤 Исраилов Рустам", callback_data="Исраилов_Рустам"),
        ],
        # [
        #     InlineKeyboardButton(text="👤 Xalilov Xusan", callback_data="xusan"),
        # ],
        # [
        #     InlineKeyboardButton(text="👤 Otabek", callback_data="otabek"),
        #     InlineKeyboardButton(text="👤 Xurshid", callback_data="xurshid"),
        # ],
        # [
        #     InlineKeyboardButton(text="👤 Miraziz Dev", callback_data="miraziz"),
        # ],
        [
            InlineKeyboardButton(text="⬅️ назад", callback_data="сотрудникиназад"),
        ],
    ],
)

отажон =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="отажонназад"),
            InlineKeyboardButton(text="🔗 По ссылке", url="https://t.me/otajonbozorboyev"),
        ],
    ],row_width=True
)

рустам = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="рустамназад"),
            InlineKeyboardButton(text="🔗 По ссылке",url="https://youtube.com"),
        ],
    ],row_width=True
)