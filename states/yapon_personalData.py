from aiogram.dispatcher.filters.state import StatesGroup, State

class Yapon_PersonalData(StatesGroup):
    yapon_qaysi_sohaga = State()
    yapon_fullname = State()
    yapon_resume = State()
    yapon_phoneNumber = State()