from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from service import *
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

class CreateCategory(StatesGroup):
    get_name = State()

@router.message(F.text == "➕ Добавить Категорию")
@router.message(Command("add_category"))
async def add_category(message: Message, state: FSMContext):
    await message.answer("Введите имя категори -->")
    await state.set_state(CreateCategory.get_name)
@router.message(CreateCategory.get_name)
async def state_name_add(message: Message, state: FSMContext):
    status = await save_category(message.text)
    if status:
        await message.answer("Категория создана!")
    else:
        await message.answer("Ошибка при создании категори!!")
    
    
    await state.clear()    
    
    
class CreateJob(StatesGroup):
    title = State()
    description = State() 
    salary = State()
    category_id = State()   
    
@router.message(F.text == "➕ Добавить вакансию")
@router.message(Command("add_job")) 
async def add_job(message: Message, state: FSMContext):
    await message.answer("Введите название вакансии")
    await state.set_state(CreateJob.title)
    
    
@router.message(CreateJob.title)
async def job_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("Введите описание вакансии")
    await state.set_state(CreateJob.description)
    
@router.message(CreateJob.description)
async def job_description(message: Message, state: FSMContext):
     await state.update_data(description=message.text)
     await message.answer("Введите зарплату")
     await state.set_state(CreateJob.salary)

@router.message(CreateJob.salary)
async def job_salary(message: Message, state: FSMContext):
     await state.update_data(salary=int(message.text))
     await message.answer("Введите ID категории")
     await state.set_state(CreateJob.category_id)
     
     
@router.message(CreateJob.category_id)
async def job_category(message: Message, state: FSMContext):
    data = await state.get_data() 
    status = await save_job(
        data["title"],
        data["description"],
        data["salary"],
        int(message.text)
    )
    if status:
        await message.answer("Вакансия создана")
    
    else:
        await message.answer("Ошибка при создании вакансии")
    
    
    await state.clear()    

 
    
 

    
    
    
    
        