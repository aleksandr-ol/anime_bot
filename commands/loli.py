import command_system
import vkapi
import random


def loli():
   # Получаем случайную картинку из пабли
   groups = [-107312056, -127518015]
   post = vkapi.repost_without_header(random.choice(groups))
   message = 'Вот тебе лолька :)\nВ следующий раз я пришлю другую.\n' + post['text']
   return message, post['attachments']

loli_command = command_system.Command()

loli_command.keys = ['лолька', 'лоли', 'loli']
loli_command.description = 'Пришлю лольку'
loli_command.process = loli
