from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def StartFunc(Message: Message):
    await Message.answer("Hello")