from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from parser import PATH_FILE_TXT
from aiogram.utils import executor

TOKEN_BOT = '5529934320:AAH4Debxx3u1kEbK-aNBPAp0yGJ60VYu2E0'

bot = Bot(token=TOKEN_BOT)
dp: Dispatcher = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message):
    await bot.send_message(message.chat.id, 'Данный бот выводит топ 10 майнеров с сайта Moonarch по команде Top')


@dp.message_handler()
async def get_top(message):
    lts_data = ""
    if not message.text.find(":") == -1:
        lts_data = message.text.split(":")
    print(lts_data)

    if message.text.upper() == "TOP":
        with open(PATH_FILE_TXT) as file:
            for line in file.readlines()[:10]:
                word = line.split(",")
                await bot.send_message(
                    message.chat.id,
                    "{0}\n{1}\n {2}\n {3}\n".format(word[2], word[0], word[1], word[3])
                )

    else:
        await bot.send_message(message.chat.id, "Команда введена неверно")

executor.start_polling(dp)

