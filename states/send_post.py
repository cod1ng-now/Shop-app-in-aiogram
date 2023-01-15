from aiogram.dispatcher.filters.state import State, StatesGroup


class SendPostState(StatesGroup):
    post = State()


class ForwardPostState(StatesGroup):
    post = State()