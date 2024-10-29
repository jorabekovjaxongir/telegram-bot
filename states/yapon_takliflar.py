from aiogram.dispatcher.filters.state import StatesGroup, State

class Yapon_PersonalData3(StatesGroup):
    yapon_text = State()
    yapon_phoneNumber = State()