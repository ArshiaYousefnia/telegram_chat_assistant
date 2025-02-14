import asyncio
import os
import logging
from dotenv import load_dotenv
from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, CallbackContext

from api import get_btc_price

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I am your bot 🤖")

async def btc_price_usd(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(get_btc_price())

def set_bot_commands(app: Application):
    commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("btc_usd", "Return current BTC USD"),
    ]
    app.bot.set_my_commands(commands)

def main():
    app = Application.builder().token(BOT_API_TOKEN).connect_timeout(30).read_timeout(30).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("btc_usd", btc_price_usd))

    set_bot_commands(app)

    app.run_polling()

if __name__ == "__main__":
    main()
