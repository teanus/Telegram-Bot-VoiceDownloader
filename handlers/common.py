#
#           Developer Contacts:
#               VK: vk.com/dimawinchester
#               Telegram: t.me/teanus
#               Github: github.com/teanus
#
#
#
# ████████╗███████╗ █████╗ ███╗   ██╗██╗   ██╗███████╗
# ╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██║   ██║██╔════╝
#    ██║   █████╗  ███████║██╔██╗ ██║██║   ██║███████╗
#    ██║   ██╔══╝  ██╔══██║██║╚██╗██║██║   ██║╚════██║
#    ██║   ███████╗██║  ██║██║ ╚████║╚██████╔╝███████║
#    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝


import shutil
from datetime import datetime
from aiogram import types, Dispatcher
from create_bot import bot
from resources import config
from languages import lang


async def start(message: types.Message):
    await message.reply(lang.message_start)


async def send_audio(message: types.Message):
    user_id = message.from_user.id
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    if config.saving():
        file_name = f'voices/{user_id}/{date}.mp3'
        await bot.download_file(file_path, file_name)
        with open(file_name, 'rb') as audio:
            await bot.send_audio(user_id, audio, performer='TEANUS', title='VoiceDownloader')
            await bot.send_message(user_id, lang.message_send_audio)
    else:
        file_name = 'temp/audio.mp3'
        await bot.download_file(file_path, file_name)
        with open(file_name, 'rb') as audio:
            await bot.send_audio(message.from_user.id, audio, performer='TEANUS', title='VoiceDownloader')
            await bot.send_message(user_id, lang.message_send_audio)
        shutil.rmtree('temp/')


async def info(message: types.Message):
    await message.reply(lang.message_info)


async def other_messages(message: types.Message):
    await message.reply(lang.message_other)


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(send_audio, content_types='voice')
    dp.register_message_handler(info, commands=['info'])
