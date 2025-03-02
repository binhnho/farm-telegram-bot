from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import os

# Lấy TOKEN từ biến môi trường
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Chào mừng bạn đến với game nông trại!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
