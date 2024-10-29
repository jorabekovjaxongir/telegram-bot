#telegram/filters/__init__.py
from aiogram import Dispatcher

from loader import dp
from .output import GetData,GetTXT
#from .In_List import ListFilter,NotListFilter
#from .IS_ADMIN import AdminFilter
if __name__ == "filters":
    dp.filters_factory.bind(GetData)
    dp.filters_factory.bind(GetTXT)
    #dp.filters_factory.bind(ListFilter)
    #dp.filters_factory.bind(AdminFilter)
    #dp.filters_factory.bind(NotListFilter)
    pass
