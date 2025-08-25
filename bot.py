from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from deep_translator import GoogleTranslator
import os

BOT_TOKEN = os.getenv("8302049150:AAEyTunuiIC3hqWQVFyYrxuuL_2vpo8um7Q")  # get token from environment

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hei! Send me English text and I’ll translate it into Finnish 🇫🇮")

async def translate_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    english_text = update.message.text
    try:
        translated = GoogleTranslator(source="en", target="fi").translate(english_text)
        await update.message.reply_text(f"**Finnish:** {translated}")
    except Exception:
        await update.message.reply_text("⚠️ Sorry, I couldn’t translate right now.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_text))
    print("Bot is running on Railway 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
