import command_system
import vkapi

def random_anime():
    anime = vkapi.get_random_anime()
    message = 'Вот твое анимэ:\n' + anime
    return message, ''

random_anime_command = command_system.Command()

random_anime_command.keys = ['посоветуй анимэ']
random_anime_command.description = 'Скину тебе название анимэ'
random_anime_command.process = random_anime