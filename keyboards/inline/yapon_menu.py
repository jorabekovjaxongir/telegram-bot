from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup 


yapon_Menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌎 メニュー", callback_data="yapon_Menu"),
            # InlineKeyboardButton(text="⬅️ 戻る", callback_data="yapon_1ortga"),
        ],
    ],row_width=True
)

yapon_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📜 私たちについて", callback_data="yapon_about"),
            InlineKeyboardButton(text="📊 コース", callback_data="yapon_kurslar"),
        ],
        [
            InlineKeyboardButton(text="👨‍💻 従業員", callback_data="yapon_xodimlar"),
            InlineKeyboardButton(text="🧾 欠員", callback_data="yapon_vakansiya"),
        ],
        [
            InlineKeyboardButton(text="🛠 設定", callback_data="yapon_sozlamalar"),
        ],
    ],row_width=True
)

yapon_aboutmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🎦 ビデオ", url="https://youtube.com/shorts/qsHai1S7wKg?si=GnAz1KR9ukhCDiNB"),
            InlineKeyboardButton(text="⬅️ 戻る", callback_data="yapon_aboutortga"),
        ],
    ],row_width=True
)

yapon_kurslarmenu =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📘 フロントエンド",callback_data="yapon_frontend"),
            InlineKeyboardButton(text="📕 バックエンド", callback_data="yapon_backend"),
        ],
        [
            InlineKeyboardButton(text="📙 サイバーセキュリティ",callback_data="yapon_kibr"),
            InlineKeyboardButton(text="📗 グラフィックデザイン",callback_data="yapon_grafik"),
        ],
        [
            InlineKeyboardButton(text="⬅️ 戻る", callback_data="yapon_kurslarortga"),
        ],
    ],row_width=True
)

yapon_informatsiya = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="⤴️ 戻る", callback_data='yapon_2ortga')
        ]
    ]
)

yapon_anketa1 = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="⤴️ 戻る", callback_data='yapon_3ortga')
        ]
    ]
)

yapon_sozlamalar_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🗣️ 言語", callback_data="yapon_Tillar" ),
            InlineKeyboardButton(text="📣 苦情と提案", callback_data="yapon_shikoyat"),
        ],
    ],row_width=True
)

yapon_shikoyat_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ 戻る",callback_data="1_戻る")
        ],
    ],
)

yapon_kurslar1= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✍️ コースの登録", callback_data="yapon_anketa"),
            InlineKeyboardButton(text="⬅️ 戻る", callback_data="yapon_ortga2"),
        ],
    ],)


yapon_xodimlarmenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👤 オタゾン・バザルバエフ", callback_data="yapon_otajon"),
            InlineKeyboardButton(text="👤 イライロフ・ロスタム", callback_data="yapon_rustamjon"),
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
            InlineKeyboardButton(text="⬅️ 戻る", callback_data="yapon_xodimlarortga"),
        ],
    ],
)

yapon_otajon =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ 戻る", callback_data="yapon_otajonortga"),
            InlineKeyboardButton(text="🔗 リンクをたどってください", url="https://t.me/otajonbozorboyev"),
        ],
    ],row_width=True
)

yapon_rustam = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ 戻る", callback_data="yapon_rustamortga"),
            InlineKeyboardButton(text="🔗 リンクをたどってください",url="https://youtube.com"),
        ],
    ],row_width=True
)