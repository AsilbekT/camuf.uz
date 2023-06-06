from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.core.exceptions import ObjectDoesNotExist
from .models import BotUsers
from django.views.decorators.csrf import csrf_exempt
import json
from .credetials import URL, BOT_API
# Create your views here.
from django.views.decorators.http import require_http_methods


def index(request):
    return HttpResponse("index is working")


def translate(message=None, user=None, text=None):
    lang = ''
    if user:
        if user.user_lang == 'uz':
            lang = user.user_lang
        elif user.user_lang == 'en':
            lang = user.user_lang
    elif message:
        user_id = message['from']['id']
        user = BotUsers.objects.get(user_id=user_id)
        if user.user_lang == 'uz':
            lang = user.user_lang
        elif user.user_lang == 'en':
            lang = user.user_lang
    else:
        return text

    if lang == 'uz':
        words = {
            "choose language": "tilni tanlang",
            "please enter your name":'iltimos ismizni kiriting'
        }
        if text in words.keys():
            return words[text]
        else:
            return text


    elif lang == 'en':
        words = {
            "tarjima tilini kiritish":"enter translating languages",
            'setting':'setting',
            'biz haqimizda': 'about us',
            "tilni tanlang": "choose language"
        }
        if text in words.keys():
            return words[text]
        else:
            return text




@csrf_exempt
def getpost(request):
    if request.method == 'POST':
        telegram_message = json.loads(request.body)

        if "message" in telegram_message.keys():
            message = telegram_message['message']

        try:
            user = BotUsers.objects.get(user_id=message['from']['id'])

            if 'text' in message.keys():
                messageHandler(message, user)

        except ObjectDoesNotExist:
            if message['text'] == translate(text="register"):
                    user = BotUsers.objects.create(user_id=message['from']['id'], user_step='get_lang')
                    user.save()
                    stepHandler(user, message)

            else:
                bot_request("sendMessage", {
                    'chat_id': message['from']['id'],
                    'text': "Botimizni ishlatish uchun registratsiyadan oting/ In order to use our bot please register!",
                    "reply_markup": json.dumps({
                        "keyboard": [[
                            'register',
                        ]],
                        'resize_keyboard': True
                    })
                })
        if 'contact' in message.keys():
            print(message)
            setHandler(message, user)


    return HttpResponse("getpost")


@require_http_methods(["GET", "POST"])
def setwebhook(request):
    response = requests.post(BOT_API + "setWebhook?url=" + URL).json()
    return HttpResponse(f"{response}")


def bot_request(method, data):
    return requests.post(BOT_API + method, data)


def messageHandler(message, user):
    # print(message)
    user = BotUsers.objects.get(user_id=message['from']['id'])
    if user.user_step:
        setHandler(message, user)
    else:
        redirectToHomePage(message)


def setHandler(message, user):
    if user.user_step:
        if user.user_step == "get_lang":
            user.user_lang = message['text']
            user.user_step = 'get_name'
            user.save()
            stepHandler(user, message)

        elif user.user_step == 'get_name':
            user.fullname = message['text']
            user.user_step = 'get_contact'
            user.save()
            stepHandler(user, message)

        elif user.user_step == 'get_contact':
            user.user_contact = message['contact']['phone_number']
            user.user_step = ''
            user.save()
            stepHandler(user, message)


def stepHandler(user, message):
    if user.user_step == "get_lang":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': 'Tilni tanlang / Choose the language',
            "reply_markup": json.dumps({
                "keyboard": [['uz'], ['en']],
                'resize_keyboard': True
            })
        })
    elif user.user_step == "get_name":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(user=user, text='iltimos ismizni kiriting'),
            "reply_markup": json.dumps({
                'remove_keyboard': True})
        })
    elif user.user_step == "get_contact":
        print('con')
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': "contactni kiriting",
            "reply_markup": json.dumps({
                "keyboard": [[{
                    'text': "contact",
                    'request_contact': True
                }]],
                'remove_keyboard': True
            })
        })
    else:
        redirectToHomePage(message)



def redirectToHomePage(message):
    user_id = message['from']['id']
    bot_request("sendMessage", {
        "chat_id": user_id,
        'text': "home page",
        "reply_markup": json.dumps({
            "keyboard": [
                [
                    translate(message=message, text="tarjima tilini kiritish"), translate(message=message, text='setting')
                ], [
                    translate(message=message, text='biz haqimizda')
                ]
            ],
            'resize_keyboard': True
        })
    })