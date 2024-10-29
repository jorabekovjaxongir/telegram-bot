from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup 

tillar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        	InlineKeyboardButton(text="🇺🇿 O'zbek",callback_data="O'zbek"),
        	InlineKeyboardButton(text="🇷🇺 Русский",callback_data="Русский"),
        ],
        [
            InlineKeyboardButton(text="🇯🇵 Yaponiya",callback_data="Yaponiya"),
            # InlineKeyboardButton(text="🇺🇸 United States",callback_data="United_States"),
        ],
        [
            # InlineKeyboardButton(text="⬅️ Ortga", callback_data="menuortga"),
            # InlineKeyboardButton(text="⬅️ Ortga", callback_data="sozlamalarortga"),
        ]
    ], row_width=True
)
