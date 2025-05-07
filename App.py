from aiogram import Bot, Dispatcher, types, executor
import json

API_TOKEN = '7605003823:AAFBTOYw6sxosgMnlMjBkeIZ2jaixXVYKEs'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = types.WebAppInfo(url="https://willowy-flan-288b7f.netlify.app/")
    button = types.KeyboardButton(text="UC Buyurtma", web_app=web_app)
    keyboard.add(button)
    await message.answer("Buyurtma berish uchun tugmani bosing:", reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def web_app_data(message: types.Message):
    data = json.loads(message.web_app_data.data)
    pubg_id = data.get("pubg_id")
    tg_user = data.get("telegram_user")
    await message.answer(f"✅ Buyurtma:\\nPUBG ID: {pubg_id}\\nTelegram: {tg_user}")

if __name__ == '__main__':
    executor.start_polling(dp)
