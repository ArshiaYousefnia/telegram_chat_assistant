import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

load_dotenv()
BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I am your bot 🤖")

def main():
    app = Application.builder().token(BOT_API_TOKEN).connect_timeout(30).read_timeout(30).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == "__main__":
    main()
