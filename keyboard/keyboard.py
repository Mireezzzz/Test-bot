from lexicon.lexicon import LEXICON_ANS

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_inline_keyboard(width: int, *args: str, **kwargs: str) -> InlineKeyboardMarkup:
    buttons: list[InlineKeyboardButton] = []

    kb_builder = InlineKeyboardBuilder()
    if args:
        for button in args:
            buttons.append(
                InlineKeyboardButton(
                    text=LEXICON_ANS[button] if button in LEXICON_ANS else button,
                    callback_data=button
                )
            )

    if kwargs:
        for button, item in kwargs.items():
            buttons.append(
                InlineKeyboardButton(
                    text=item,
                    callback_data=button
                )
            )

    kb_builder.row(width=width, *buttons)

    return kb_builder.as_markup()

