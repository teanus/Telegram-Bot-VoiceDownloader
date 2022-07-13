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


import yaml
from resources import config
from pathlib import Path

path = Path.cwd() / 'languages' / f'{config.locale()}.yaml'


def read_yaml():
    with open(path, "r", encoding='utf-8') as file:
        return yaml.safe_load(file)


message_start = read_yaml()['message_start']
message_send_audio = read_yaml()['message_send_audio']
message_info = read_yaml()['message_info']
message_other = read_yaml()['message_other']
