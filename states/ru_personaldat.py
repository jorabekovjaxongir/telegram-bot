from aiogram.dispatcher.filters.state import StatesGroup, State

class ru_personalData(StatesGroup):
    ru_qaysi_sohaga = State()
    ru_fullname = State()
    ru_resume = State()
    ru_phoneNumber = State() 