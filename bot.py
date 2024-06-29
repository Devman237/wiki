import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart ,command
from aiogram.types import Message
from m import WikipediaFunction
# Bot token can be obtained via https://t.me/BotFather
TOKEN ="7076783750:AAHSr7q_d5nW8J7HH6FOYvnf8_m60WEJnS0"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

@dp.message(command.Command("uz"))
async def set_lang(message:Message):
    await message.answer("O'zbek tiliga ozgartitilidi")



@dp.message(command.Command("en"))
async def set_lang(message:Message):
    await message.answer("Turn to english")    
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}\n ingliz tilin tanlash uchun /en bosing \n rus tiliga otkazish uchun /ru bosing \n qayta ozbektiliga otkazish uchun /uz bosing")


@dp.message()
async def echo_handler(message: Message):
    malumot = WikipediaFunction(malumot=message.text)
    await message.answer(malumot)
    

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
