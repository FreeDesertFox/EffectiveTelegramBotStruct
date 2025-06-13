
import asyncio
from aiogram import Bot, Dispatcher

class EventHandler():
    def __init__(self, Bot: Bot, Dispatcher: Dispatcher, Routers: list, Url: str = None):
        self.Bot = Bot
        self.Dispatcher = Dispatcher

        for Router in Routers:
            self.Dispatcher.include_router(Router)

        if Url:
            self.__webhook__(Url)

        else:
            asyncio.run(self.__longpolling_());
            
    async def __webhook__(self, Url):
        pass

    async def __longpolling_(self):
        await self.Dispatcher.start_polling(self.Bot)