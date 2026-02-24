import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Tokeni Heroku-dan götürəcək
API_TOKEN = os.getenv("BOT_TOKEN") 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Düyməni yaradırıq
    markup = InlineKeyboardMarkup()
    
    # Sənin GitHub Pages linkin (bura öz linkini yaz)
    site_url = "https://xeyaldi.github.io/ht-bots/" 
    
    # WebAppInfo istifadə etdiyimiz üçün o kvadrat ikon avtomatik düşəcək
    markup.add(InlineKeyboardButton(
        text="HT BOTS - DAXİL OL 🚀", 
        web_app=WebAppInfo(url=site_url)
    ))
    
    # Sənin istədiyin xüsusi mətn
    welcome_text = (
        "HT BOTS-a xoş gəlmisiniz! \n\n"
        "Aşağıdakı düyməyə basaraq proqramımıza daxil olub "
        "botlarımızla tanış ola və onlar haqqında rəy bildirə bilərsiniz 👇"
    )
    
    await message.answer(welcome_text, reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
