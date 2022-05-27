from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('Курс Долора')
    ],
    [
        KeyboardButton('Биткойн Долора'),
        KeyboardButton('Биткойн Рублей'),
    ]
   
], resize_keyboard=True, one_time_keyboard=True)
