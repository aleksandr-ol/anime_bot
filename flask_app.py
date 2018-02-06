
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, json
from settings import *
import messageHandler
import vkapi
import random

dict = {}

with open("mysite/list_of_phrases.txt") as file:
    for line in file:
        key, *value = line.split('\\')
        if key in dict:
            dict[key].append(value[0])
        else:
            dict[key] = [value[0]]

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        if data['object']['body'] in dict:
            user_id = data['object']['user_id']
            message = random.choice(dict[data['object']['body']])
            vkapi.send_message(user_id, token, message, '')
            return 'ok'
        messageHandler.create_answer(data['object'], token)
        return 'ok'
