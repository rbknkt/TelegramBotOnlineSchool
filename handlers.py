import keyboards

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

router = Router()

# команда /start
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("команда /start")
