from scripts import *
from config import *
global url
import aiogram

bot = aiogram.Bot(token=token)
dp = aiogram.Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def parse(msg:aiogram.types.Message):
    await msg.answer(await msg.answer(Avitoparse(url = 'https://www.avito.ru/moskva/zapchasti_i_aksessuary/zapchasti/dlya_avtomobiley/tormoznaya_sistema-ASgBAgICA0QKJKwJ~GPiDNi1AQ?cd=1&p=2&q=%D1%82%D0%BE%D1%80%D0%BC%D0%BE%D0%B7%D0%BD%D1%8B%D0%B5+%D1%82%D1%80%D1%83%D0%B1%D0%BA%D0%B8', count = 10, items = ['тормозная трубка']).parse()))





if __name__ == '__main__':
    aiogram.executor.start_polling(dp)