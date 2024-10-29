from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData3(StatesGroup):
    fullname = State()
    phoneNumber = State()