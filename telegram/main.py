from aiogram import Bot,Dispatcher,types,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN='5784225579:AAEwdedj7VC6hzlFIQHsw7fUNboIWBzt-cc'

bot=Bot(token=TOKEN)
dp=Dispatcher(bot,storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def send_start(message:types. Message):
    await message.answer(text='Hi')



@dp.message_handler(commands=['help'])
async def send_help(message:types.Message):
    await message.answer(text='if you need help')




@dp.message_handler(commands=['button'])
async def send_button(message:types.Message):
    keybord=types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    button1=types.KeyboardButton(text="I'm button")
    button2=types.KeyboardButton(text="GitHub")
    keybord.add(button1,button2)
    await message.answer(text='Press Button',reply_markup=keybord)



@dp.message_handler(commands=['url'])
async def send_url(message:types.Message):
    buttons=[
        types.InlineKeyboardButton(text="GitHub", url="https://github.com/gareflecioner/hello_world.git"),
        types.InlineKeyboardButton(text="FSM", url="https://lolz.guru/threads/3769612/")
    ]
    KeybordInline=types.InlineKeyboardMarkup()
    KeybordInline.add(*buttons)
    await message.answer(text="make a choice",reply_markup=KeybordInline)


if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)


