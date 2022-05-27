import logging
from pycoingecko import CoinGeckoAPI
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import TOKEN
# from Booton import defind
from Booton import keyboard
from parser_usd import main

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
async def on_start(_):
    print('Бот запущен')
    
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
cg = CoinGeckoAPI()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)
    
    await message.reply('<b>Hello</b>',
                        parse_mode='HTML')
    # await message.reply(f'bitcoin {bitcoin_usd}')
@dp.message_handler(lambda message: message.text == "Курс Долора")
async def dollar_exchange(message: types.Message):
    cur = main()
    await message.reply(f'<b>Доллар США {cur} Рублей</b>',
    parse_mode='HTML')

@dp.message_handler(lambda message: message.text == "Биткойн Долора")
async def bitcoin_dolor(message: types.Message):
    USD = cg.get_price(ids='bitcoin', vs_currencies='usd')
    bitcoin_usd = USD['bitcoin']['usd']
    await message.reply(f'<b>Биткойн {bitcoin_usd} Долора</b>',
    parse_mode='HTML')

@dp.message_handler(lambda message: message.text == "Биткойн Рублей")
async def bitcoin_rubles(message: types.Message):
    RUB = cg.get_price(ids='bitcoin', vs_currencies='rub')
    bitcoin_rub = RUB['bitcoin']['rub']
    await message.reply(f'<b>Биткойн {bitcoin_rub} Рублей👁</b>',
    parse_mode='HTML')


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)