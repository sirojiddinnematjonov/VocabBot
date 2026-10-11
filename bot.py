import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import MenuButtonWebApp, WebAppInfo, ReplyKeyboardRemove

BOT_TOKEN = "8821234462:AAFRgNLvXnAtXY4yePXCuV2aSR-Jg6_5h4s"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

WEB_APP_URL = "https://sirojiddinnematjonov.github.io/VocabBot/"

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    # Pastdagi chap burchakdagi "Open" tugmasini o'rnatamiz
    await bot.set_chat_menu_button(
        chat_id=message.chat.id,
        menu_button=MenuButtonWebApp(text="Open", web_app=WebAppInfo(url=WEB_APP_URL))
    )
    
    welcome_text = (
        f"Assalomu alaykum, {message.from_user.first_name}! 👋\n\n"
        "**VocabBot**ga xush kelibsiz! 📚\n\n"
        "Bu bot orqali siz ingliz tili so'zlarini fleshkardlar yordamida oson va samarali yodlashingiz mumkin.\n\n"
        "✨ **Imkoniyatlar:**\n"
        "• Yangi so'zlar va ularning tarjimasini qo'shish\n"
        "• Fleshkardlar orqali so'zlarni takrorlash va yodda saqlash\n"
        "• O'z lug'atingizni boshqarish\n\n"
        "👇 Boshlash uchun pastki chap burchakdagi **'Open'** tugmasini bosing!"
    )
    
    # reply_markup=ReplyKeyboardRemove() eski klaviatura va tugmalarni majburan o'chiradi
    await message.answer(
        welcome_text, 
        parse_mode="Markdown", 
        reply_markup=ReplyKeyboardRemove()
    )

async def main():
    print("Bot muvaffaqiyatli ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())