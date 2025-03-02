from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import os
import asyncio

# Lấy TOKEN từ biến môi trường
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Chào mừng bạn đến với game nông trại!")

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot đang chạy...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
    
