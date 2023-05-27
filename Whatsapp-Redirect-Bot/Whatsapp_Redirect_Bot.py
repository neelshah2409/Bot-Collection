import logging
import re
from os import environ

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, Response
from telegram.bot import Bot
from telegram.chataction import ChatAction
from telegram.parsemode import ParseMode
from telegram.update import Update
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram.error import TelegramError

from dotenv import load_dotenv

from helper import logger

load_dotenv()  # take environment variables from .env.

DOMAIN = environ.get("DOMAIN")
BOT_TOKEN = environ.get("BOT_TOKEN")

try:
    assert DOMAIN != None
    assert BOT_TOKEN != None
except AssertionError:
    logger.critical("Please set the environment variables")
    exit(1)

try:
    bot = Bot(BOT_TOKEN)
except (TypeError, TelegramError):
    logger.critical("⚠️ Invalid bot token")
    exit(1)

app = FastAPI()


@app.get("/")
async def index():
    return HTMLResponse("")


@app.get("/robots.txt")
async def robots():
    return HTMLResponse("User-agent: *\nDisallow: /")


@app.get("/favicon.ico")
async def favicon():
    with open("favicon.png", "rb") as f:
        return Response(content=f.read(), media_type="image/png")


async def cmd_start(update: Update):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hello {update.effective_user.full_name} 👋🏻<br>Please send a phone number you want to chat with including international code",
    )


async def cmd_help(update: Update):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="You can send the phone number you want to chat with <b>including international code</b> (eg +447419651046)",
        parse_mode=ParseMode.HTML,
    )


async def wrong_number(update: Update):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="❌ Wrong number",
    )


async def phone_handler(update: Update):
    bot.send_message(
        text="ok",
        chat_id=update.effective_chat.id,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🔗 Open chat",
                        url=f"https://api.whatsapp.com/send?phone={update.effective_message.text.replace(' ','').replace('-','')}&text=",
                    )
                ]
            ]
        ),
    )


async def update_handler(update: Update):
    try:
        if update.effective_message and update.effective_message.text:
            bot.send_chat_action(
                chat_id=update.effective_chat.id, action=ChatAction.TYPING
            )
            if update.effective_message.text == "/start":
                await cmd_start(update)
            elif update.effective_message.text == "/help":
                await cmd_help(update)
            elif re.fullmatch("\+[0-9\s?\-?]{5,20}", update.effective_message.text):
                await phone_handler(update)
            else:
                await wrong_number(update)
        else:
            await cmd_help(update)
    except (AttributeError, TelegramError) as err:
        logging.error(f"🔴 Exception!: {err}\nupdate: {update}")


@app.post("/telegram-update-4e1cb6")
async def webhook_handler(request: Request):
    data = await request.json()
    upcoming_update = Update.de_json(data, bot=bot)
    await update_handler(upcoming_update)
    return "ok"


@app.get("/setwebhook-f443dc992ba6")
async def set_webhook():
    s = bot.set_webhook(url=f"{DOMAIN}/telegram-update-4e1cb6")
    if s:
        return HTMLResponse("ok")
    else:
        return HTMLResponse("Error!")
