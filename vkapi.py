import vk
import random
import settings

session = vk.Session()
api = vk.API(session, v=5.69)


def repost_without_header(group_id):
    max_num = api.wall.get(owner_id=group_id, access_token=settings.service_key, filter='owner')['count']
    num = random.randint(1, max_num)
    post = api.wall.get(owner_id=group_id, offset=num, count=1, access_token=settings.service_key, filter='owner')['items'][0]
    response = {}
    response['text'] = post['text']
    response['attachments'] = ''
    for attachment in post['attachments']:
        response['attachments'] += attachment['type'] + str(attachment[attachment['type']]['owner_id']) + '_' + str(attachment[attachment['type']]['id']) + ','

    return response


def get_random_wall_post(group_id):
    max_num = api.wall.get(owner_id=group_id, access_token=settings.service_key, filter='owner')['count']
    num = random.randint(1, max_num)
    post = api.wall.get(owner_id=group_id, offset=num, count=1, access_token=settings.service_key, filter='owner')['items'][0]
    attachment = 'wall' + str(post['owner_id']) + '_' + str(post['id'])

    return attachment


def get_random_anime():
    with open("mysite/advise_anime.txt") as file:
        anime_array = [row.strip() for row in file]

    return anime_array[random.randint(0, len(anime_array) - 1)]




def send_message(user_id, token, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)

