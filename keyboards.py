from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def category_batton():
    keybor = ReplyKeyboardMarkup(
        keyboard= [
            [KeyboardButton(text="📋 Показать категори")],
            [KeyboardButton(text="📋 Показать вакансии")],
            [KeyboardButton(text="➕ Добавить Категорию")],
            [KeyboardButton(text="➕ Добавить вакансию")],
            [KeyboardButton(text="Изменить категори")],
            [KeyboardButton(text="Удалить Категорию")],
            
        ], resize_keyboard=True   
    )
    return keybor