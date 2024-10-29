from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData(StatesGroup):
    qaysi_sohaga = State()
    fullname = State()
    resume = State()
    phoneNumber = State()