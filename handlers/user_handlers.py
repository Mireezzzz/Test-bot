from lexicon.lexicon import LEXICON_CMD, LEXICON_QUE, LEXICON_ANS
from keyboard.keyboard import create_inline_keyboard
from states.states import FSMPassingTest
from google_sheets.table import add_result, get_answer
from utils.check_answers import check_answer

from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

router = Router()


# Хендлер на команду /start
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        text=LEXICON_CMD[message.text]
    )


# Хендлер на команду /help
@router.message(Command(commands='help'))
async def cmd_help(message: Message):
    await message.answer(
        text=LEXICON_CMD[message.text]
    )


# Хендлер на команду /test
@router.message(Command(commands='test'))
async def cmd_test(message: Message):
    await message.answer(
        text=LEXICON_CMD[message.text],
        reply_markup=create_inline_keyboard(1,
                                            'start',
                                            'cancel')
    )


@router.callback_query(F.data == "start")
async def ask_one_question(callback: CallbackQuery, state: FSMContext):
    await state.set_state(FSMPassingTest.passing_test)
    await callback.message.edit_text(
        text=LEXICON_QUE['first'],
        reply_markup=create_inline_keyboard(1,
                                            "first_question_answer_one",
                                            "first_question_answer_two",
                                            "first_question_answer_three",
                                            "first_question_answer_four"
                                            )
    )
    await callback.answer()


@router.callback_query(F.data == "cancel")
async def cancel_process(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Очень жаль;(\n"
             "Если захочешь пройти тест набери команду /test"
    )


@router.callback_query(StateFilter(FSMPassingTest.passing_test), F.data.in_(["first_question_answer_one",
                                                                             "first_question_answer_two",
                                                                             "first_question_answer_three",
                                                                             "first_question_answer_four"]))
async def ask_two_question(callback: CallbackQuery, state: FSMContext):
    await state.update_data(one=LEXICON_ANS[callback.data])
    await callback.message.edit_text(
        text=LEXICON_QUE['second'],
        reply_markup=create_inline_keyboard(1,
                                            "second_question_answer_one",
                                            "second_question_answer_two",
                                            "second_question_answer_three",
                                            "second_question_answer_four")
    )
    await callback.answer()


@router.callback_query(StateFilter(FSMPassingTest.passing_test), F.data.in_(["second_question_answer_one",
                                                                             "second_question_answer_two",
                                                                             "second_question_answer_three",
                                                                             "second_question_answer_four"]))
async def ask_three_question(callback: CallbackQuery, state: FSMContext):
    await state.update_data(two=LEXICON_ANS[callback.data])
    await callback.message.edit_text(
        text=LEXICON_QUE['third'],
        reply_markup=create_inline_keyboard(1,
                                            "third_question_answer_one",
                                            "third_question_answer_two",
                                            "third_question_answer_three",
                                            "third_question_answer_four"
                                            )
    )
    await callback.answer()


@router.callback_query(StateFilter(FSMPassingTest.passing_test), F.data.in_(["third_question_answer_one",
                                                                             "third_question_answer_two",
                                                                             "third_question_answer_three",
                                                                             "third_question_answer_four"]))
async def ask_fourth_question(callback: CallbackQuery, state: FSMContext):
    await state.update_data(three=LEXICON_ANS[callback.data])
    await callback.message.edit_text(
        text=LEXICON_QUE['fourth'],
        reply_markup=create_inline_keyboard(1,
                                            "fourth_question_answer_one",
                                            "fourth_question_answer_two",
                                            "fourth_question_answer_three",
                                            "fourth_question_answer_four"
                                            )
    )
    await callback.answer()


@router.callback_query(StateFilter(FSMPassingTest.passing_test), F.data.in_(["fourth_question_answer_one",
                                                                             "fourth_question_answer_two",
                                                                             "fourth_question_answer_three",
                                                                             "fourth_question_answer_four"]))
async def ask_fifth_question(callback: CallbackQuery, state: FSMContext):
    await state.update_data(four=LEXICON_ANS[callback.data])
    await callback.message.edit_text(
        text=LEXICON_QUE['fifth'],
        reply_markup=create_inline_keyboard(1,
                                            "fifth_question_answer_one",
                                            "fifth_question_answer_two",
                                            "fifth_question_answer_three",
                                            "fifth_question_answer_four"
                                            )
    )
    await callback.answer()


@router.callback_query(StateFilter(FSMPassingTest.passing_test), F.data.in_(["fifth_question_answer_one",
                                                                             "fifth_question_answer_two",
                                                                             "fifth_question_answer_three",
                                                                             "fifth_question_answer_four"]))
async def process_end_test(callback: CallbackQuery, state: FSMContext):
    await state.update_data(five=LEXICON_ANS[callback.data])
    data = await state.get_data()
    await state.clear()
    await callback.message.edit_text(
        text=LEXICON_QUE['end'] + check_answer(data)
    )
    await callback.answer()
    add_result(callback.message.chat.id, callback.from_user.first_name, [ans for ans in data.values()],
               "google_sheets/test-bot-418414-e4e2bdddaeca.json")
