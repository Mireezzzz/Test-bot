from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.redis import RedisStorage, Redis

redis = Redis(host='localhost')

storage = RedisStorage(redis=redis)


class FSMPassingTest(StatesGroup):
    passing_test = State()
