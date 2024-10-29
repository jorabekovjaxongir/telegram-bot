from aiogram.dispatcher.filters.state import StatesGroup, State

class Yapon_PersonalData1(StatesGroup):
    yapon_fullname = State()
    yapon_phoneNumber = State()