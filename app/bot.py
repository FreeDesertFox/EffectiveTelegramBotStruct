from config import settings
from log import StartLogging
from events import EventHandler
from handlers import router

from aiogram import Bot, Dispatcher, Router

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

class BotHandler(EventHandler):
    def __init__(self):
        StartLogging("file")

        bot = Bot(settings.BOT_TOKEN.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        dispatcher = Dispatcher()

        Routers = [router]

        super().__init__(bot, dispatcher, Routers)


if __name__ == "__main__":
    BotHandler()
