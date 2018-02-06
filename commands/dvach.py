import command_system
import vkapi
import random


def dvach():
   # Получаем случайную картинку из пабли
   post = vkapi.repost_without_header(-22751485)
   message = 'Держи :)\n' + post['text']
   return message, post['attachments']

dvach_command = command_system.Command()

dvach_command.keys = ['двач']
dvach_command.description = 'Пришлю пост с двача'
dvach_command.process = dvach
