from aiogram.dispatcher.filters.state import StatesGroup, State

class Rus_PersonalData1(StatesGroup):
    rus_fullname = State()
    rus_phoneNumber = State()