from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData1(StatesGroup):
    fullname = State()
    phoneNumber = State()