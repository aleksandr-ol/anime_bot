import command_system
import vkapi
import random


def mem():
   # Получаем случайную картинку из пабли
   groups = [-37763998, -123625539]
   post = vkapi.repost_without_header(random.choice(groups))
   message = 'Держи :)\n' + post['text']
   return message, post['attachments']

mem_command = command_system.Command()

mem_command.keys = ['покажи мем', 'мем', 'мемасик', 'мемас', 'мемчик', 'mem']
mem_command.description = 'Пришлю мем'
mem_command.process = mem
