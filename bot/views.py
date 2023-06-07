from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.core.exceptions import ObjectDoesNotExist
import urllib.request
from app.choices import SCHOOL_CHOICES, SOCIAL_STATUS, COUNTRY_CHOICES_TELEGRAM
from .models import BotUsers, BotAdmin
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.timezone import make_naive
from .credentials import URL, BOT_API, TOKEN, BASE_DOMAIN
# Create your views here.
from django.views.decorators.http import require_http_methods
from app.models import UndergraduateCourse, AppliedStudents
from django.core.files import File
from django.contrib.auth.models import Group
import datetime
import pandas as pd
import os

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
            "statistika": "📊 Statistika",
            "iltimos pasport nusxasini joylang": "Iltimos pasport nusxasini elektron shaklda jo'nating",
            "iltimos username izni kiriting": "Iltimos, username izni kiriting",
            'setting': '⚙️ Sozlash',
            "contactni kiriting": "Quyidagi tugma orqali telefon raqamingizni kiriting",
            "apply to uni": "📄 Qabul",
            "phone": "Telefon raqam",
            "contact": "📞 Telefon raqam",
            "biz haqimizda": "🎓 Universitetimiz haqida®",
            "choose language": "tilni tanlang",
            "please enter your name":'Iltimos ismizni kiriting',
            "home page": "Sizga qanday yordam berishimiz haqida bizga xabar berish uchun quyidagi variantlardan birini tanlang!",
            "Til": "Tillar 🇺🇿 🇺🇸",
            "quyidagilardan birini tanlang": "Quyidagilardan birini tanlang",
            "Muloqot tili": "Joriy til",
            "O'zbekcha": "🇺🇿 O'zbek",
            "English": "🇺🇸 Ingliz",
            "about_us_text": "Central Asian Medical University nodavlat ta‘lim muassasasiga 2022-yil 6- sentabr sanasida O‘zbekiston Respublikasi Vazirlar Maxkamasi huzuridagi Ta’lim sifatini nazorat qilish davlat inspeksiyasi tomonidan №037700 raqamli litsensiya berildi. Shu hujjat asosida universitet o‘z faoliyatini boshladi.",
            "admission_text": "'Central Asian Medical University'ga xush kelibsiz!\nBiz sizni universitetimizga kelgusi oʻquv yili uchun taklif qilishdan mamnunmiz. 'Central Asian Medical University'da biz sizga jahon andozalari darajasidagi ta’lim berish hamda tanlagan sohangizda muvaffaqiyatga erishish uchun zarur bo‘lgan bilim va ko‘nikmalar bilan ta’minlash uchun mo‘ljallangan turli xil dasturlarni taklif etamiz.",
            "Stomatologiya": "🦷 Stomatologiya",
            "Davolash ishi": "💊 Davolash ishi",
            "Pediatriya": "💉️️ Pediatriya",
            "Iltimos quyidagilardan tanlang": "Itimos quyidagilardan birini tanlang",
            "all": "Hammasi",
            "today": "Bugungilik",
            "last_week": "Bir haftalik",
            "iltimos ismizni kiriting": "Iltimos, ismizni kiriting",
            "iltimos famliyezni kiriting": "Iltimos, familiyangizni kiriting",
            "iltimos otezni ismini kiriting": "Iltimos, otezni ismini kiriting",
            "iltimos pasport raqamini kiriting": "Iltimos, pasport va serial raqamini kiriting",
            "iltimos davlatizni kiriting": "Iltimos, mamlakatingizga kiring",
            "iltimos viloyatni kiriting": "Iltimos, viloyatingizni kiring",
            "iltimos tumanni kiriting": "Iltimos, tumaningizni kiriting",
            "iltimos bitirgan bilim yurtini kiriting": "Iltimos, bitirgan bilim yurtingizni kiriting",
            "iltimos ijtimoiy holatni kiriting": "Iltimos, ijtimoiy holatingizni kiriting",
            "iltimos tel nomerni kiriting": "Iltimos, telefon raqamingizni kiriting",
            "qabul qilindi": "Sizni so'rovingiz qabul qilindi, javobini tez orada xabar qilamiz. Iltimos bizni ijtimoiy tarmoqlarda kuzatib boring."

        }
        if text in words.keys():
            return words[text]
        else:
            return text


    elif lang == 'en':
        words = {
            "iltimos username izni kiriting": "Please enter your username",
            "iltimos pasport nusxasini joylang": "Please send us an e-version of your passport copy.",
            "statistika": "📊 Statistics",
            "Iltimos quyidagilardan tanlang": "Please choose one of the following",
            "tarjima tilini kiritish":"enter translating languages",
            'setting':'⚙️ Setting',
            "contact": "📞 Phone number",
            "phone": "Phone number",
            "apply to uni": "📄 Admission",
            'biz haqimizda': '🎓 About us®',
            "tilni tanlang": "Choose language",
            "please enter your name":'Please enter your name',
            "contactni kiriting": "Please enter your phone number via the button bellow!",
            "home page": "Please select an option below to let us know how we can assist you!",
            "all": "All",
            "today": "Today",
            "last_week": "Last week",
            "Til": "Languages 🇺🇿 🇺🇸",
            "quyidagilardan birini tanlang": "Choose one of the following",
            "Muloqot tili": "Current language",
            "O'zbekcha": "🇺🇿 Uzbek",
            "English": "🇺🇸 English",
            "about_us_text": "Central Asian University's non-state educational medicine program obtained License No. 037700 from the State Inspectorate for Quality Control of Education under the Cabinet of Ministers of the Republic of Uzbekistan on September 6, 2022. The university was established based on this license.",
            "admission_text": "Welcome to Central Asian University!\nWe are delighted to invite you to join our esteemed institution for the upcoming academic year. At Central Asian University, we offer a diverse range of programs designed to provide you with a world-class education and equip you with the knowledge and skills necessary for success in your chosen field.",
            "Stomatologiya": "🦷 Dentistry",
            "Davolash ishi": "💊 General Medicine",
            "Pediatriya": "💉️️ Pediatrics",
            "iltimos ismizni kiriting": "Please enter your name",
            "iltimos famliyezni kiriting": "Please enter your surname",
            "iltimos otezni ismini kiriting": "Please enter your father's name",
            "iltimos pasport raqamini kiriting": "Please enter your passport and serial number",
            "iltimos davlatizni kiriting": "Please enter your country",
            "iltimos viloyatni kiriting": "Please enter your region",
            "iltimos tumanni kiriting": "Please enter your district",
            "iltimos bitirgan bilim yurtini kiriting": "Please choose your schooling",
            "iltimos ijtimoiy holatni kiriting": "Please choose your social status",
            "iltimos tel nomerni kiriting": "Please enter your phone number",
            "qabul qilindi": "Your application has been received, we will inform you about the answer soon. Please follow us on social media."

        }
        if text in words.keys():
            return words[text]
        else:
            return text




@csrf_exempt
def getpost(request):
    if request.method == 'POST':
        telegram_message = json.loads(request.body)
        private = True
        if 'callback_query' in telegram_message.keys():
            message = telegram_message["callback_query"]['message']
            callbackHandler(telegram_message['callback_query'])

        elif 'message' in telegram_message.keys():
            message = telegram_message['message']
            if "chat" in message.keys():
                if message['chat']['type'] == 'private':
                    private = True
        elif 'edited_message' in telegram_message.keys():
            message = telegram_message['edited_message']
            if "chat" in message.keys():
                if message['chat']['type'] == 'private':
                    private = True

        else:
            message = {}

        if private:
            try:
                user = BotUsers.objects.get(user_id=message['from']['id'])
                if is_bot_admin(user):
                    if "document" in message.keys():
                        setHandler(message=message, user=user)
                    elif 'text' in message.keys():
                        messageHandler(message, user, admin=True)
                    elif 'contact' in message.keys():
                        contactHandler(message)
                else:
                    if "document" in message.keys():
                        setHandler(message=message, user=user)
                    elif 'text' in message.keys():
                        messageHandler(message, user)
                    elif 'contact' in message.keys():
                        contactHandler(message)

            except ObjectDoesNotExist:
                if "text" in message.keys():
                    if message['text'] == translate(text="📂 Register/ A'zo bo'lish"):
                            user = BotUsers.objects.create(user_id=message['from']['id'], user_step='get_lang')
                            user.save()
                            stepHandler(user, message)

                    else:
                        bot_request("sendMessage", {
                            'chat_id': message['from']['id'],
                            'text': "Botimizni ishlatish uchun registratsiyadan o'ting/ In order to use our bot please register!",
                            "reply_markup": json.dumps({
                                "keyboard": [[
                                    "📂 Register/ A'zo bo'lish",
                                ]],
                                'resize_keyboard': True
                            })
                        })
            


    return HttpResponse("getpost")


@require_http_methods(["GET", "POST"])
def setwebhook(request):
    response = requests.post(BOT_API + "setWebhook?url=" + URL).json()
    return HttpResponse(f"{response}")

def is_bot_admin(bot_user):
    return bot_user.bot_users.exists()

def bot_request(method, data):
    return requests.post(BOT_API + method, data)



def messageHandler(message, user, admin=False):
    user = BotUsers.objects.get(user_id=message['from']['id'])
    if user.user_step:
        setHandler(message, user)
    elif message['text'] == translate(message=message, text="statistika"):
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(message=message, text="Iltimos quyidagilardan tanlang"),
            "reply_markup": json.dumps({
                "keyboard": [
                    [translate(message=message, text=i.title) for i in UndergraduateCourse.objects.all()],
                    ],
                'resize_keyboard': True
            })
        })

    elif message['text'] == translate(message=message, text="Stomatologiya"):
        statisticsHandler(user, 'Stomatologiya')
    elif message['text'] == translate(message=message, text="Pediatriya"):
        statisticsHandler(user, "Pediatriya")
    elif message['text'] == translate(message=message, text="Davolash ishi"):
        statisticsHandler(user, "Davolash ishi")


    elif message['text'] == translate(message=message, text="setting"):
        settingHandler(message)
    elif message['text'] == translate(message=message, text="apply to uni"):
        admissionHandler(message)
    elif message['text'] == translate(message=message, text='biz haqimizda'):
        bot_request("sendPhoto", {
            "chat_id": user.user_id,
            "photo": 'https://camuf.uz/static/images/logo.png',
            'parse_mode': 'html',
            'caption': translate(user=user, text="about_us_text"),
        })
    # 
    else:
        redirectToHomePage(message, admin=admin)


def statisticsHandler(user, program):
    bot_request('sendMessage', {
        'chat_id':user.user_id,
        'parse_mode': 'html',
        'text': translate(user=user, text="Iltimos quyidagilardan birini tanlang"),
        'reply_markup': json.dumps(
            {
                "inline_keyboard": [
                    [
                        {'text': translate(text="all", user=user), 'callback_data': f"all/{program}"},
                        {'text': translate(text="today", user=user), 'callback_data': f"today/{program}"},
                    ],[
                        {'text': translate(text="last_week", user=user), 'callback_data': f"last_week/{program}"}
                    ]
                ]
            }
        )
    }
                )

def setHandler(message, user):
    if user.user_step:
        if user.user_step == "get_admission_name":
            applied_student = AppliedStudents.objects.get(bot_id=user.user_id)
            applied_student.name = message['text']
            user.user_step = 'get_admission_surname'
            applied_student.save()
            user.save()
            stepHandler(user, message)

        elif user.user_step == "get_admission_surname":
            applied_student = AppliedStudents.objects.get(bot_id=user.user_id)
            applied_student.surname = message['text']
            user.user_step = 'get_admission_fathers_name'
            applied_student.save()
            user.save()

            stepHandler(user, message)
        
        elif user.user_step == "get_admission_fathers_name":
            applied_student = AppliedStudents.objects.get(bot_id=user.user_id)
            applied_student.fathers_name = message['text']
            user.user_step = 'get_admission_passport_number'
            applied_student.save()
            user.save()

            stepHandler(user, message)

        elif user.user_step == "get_admission_passport_number":
            applied_student = AppliedStudents.objects.get(bot_id=user.user_id)
            applied_student.passport_number = message['text']
            user.user_step = 'get_admission_passport_pdf'
            applied_student.save()
            user.save()
            stepHandler(user, message)
        
        elif user.user_step == "get_admission_passport_pdf":
            if "document" in message.keys():
                handlePdffiles(message, "passport_pdf")
                user.user_step = 'get_admission_country'
                user.save()
            stepHandler(user, message)

        elif user.user_step == "get_admission_country":
            applied_student = AppliedStudents.objects.get(bot_id=user.user_id)
            applied_student.country = message['text']
            user.user_step = 'get_admission_region'
            applied_student.save()
            user.save()
            stepHandler(user, message)

        elif user.user_step == "get_admission_region":
            applied_student = AppliedStudents.objects.get(bot_id=user.user_id)
            applied_student.region = message['text']
            user.user_step = 'get_admission_district'
            applied_student.save()
            user.save()
            stepHandler(user, message)

        elif user.user_step == "get_admission_district":
            applied_student = AppliedStudents.objects.get(bot_id=user.user_id)
            applied_student.district = message['text']
            user.user_step = 'get_admission_schooling'
            applied_student.save()
            user.save()
            stepHandler(user, message)
        
        elif user.user_step == "get_admission_schooling":
            applied_student = AppliedStudents.objects.get(bot_id=user.user_id)
            applied_student.schooling = message['text']
            user.user_step = 'get_admission_schooling_file'
            applied_student.save()
            user.save()
            stepHandler(user, message)

        elif user.user_step == "get_admission_schooling_file":
            if "document" in message.keys():
                handlePdffiles(message, "schooling_file")
                user.user_step = 'get_admission_social_status'
                user.save()
            stepHandler(user, message)

        elif user.user_step == "get_admission_social_status":
            applied_student = AppliedStudents.objects.get(bot_id=user.user_id)
            applied_student.social_status = message['text']
            if message['text'] != translate(message=message, text="Yo'q"):
                user.user_step = 'get_admission_social_status_file'
                applied_student.save()
                user.save()
            else:
                user.user_step = 'get_admission_phone_number'
                applied_student.save()
                user.save()

            stepHandler(user, message)

        elif user.user_step == "get_admission_social_status_file":
            if "document" in message.keys():
                handlePdffiles(message, "social_status_file")
                user.user_step = 'get_admission_phone_number'
                user.save()
            stepHandler(user, message)


        elif user.user_step == "get_admission_phone_number":
            applied_student = AppliedStudents.objects.get(bot_id=user.user_id)
            applied_student.phone_number = message['text']
            user.user_step = ''
            applied_student.save()
            user.save()

            bot_request('sendMessage', {
                'chat_id': user.user_id,
                'parse_mode': 'html',
                'text': translate(user=user, text="qabul qilindi")
                })
            text = f"<b>Yangi arizachi</b>\n"
            text += f"<b>Yo'nalish:</b> {applied_student.program.title}\n"
            text += f"<b>Familiyasi:</b> {applied_student.surname}\n"
            text += f"<b>Ismi:</b> {applied_student.name}\n"
            text += f"<b>Otasining ismi:</b> {applied_student.fathers_name}\n"
            text += f"<b>Passport raqami:</b> {applied_student.passport_number}\n"
            text += f"<b>Passport PDF:</b> \nhttps://camuf.uz{applied_student.get_passport_pdf_url()}\n"
            text += f"<b>Region:</b> {applied_student.region}\n"
            text += f"<b>O'qish:</b> {applied_student.schooling}\n"
            text += f"<b>Diplom raqami:</b> \nhttps://camuf.uz/{applied_student.get_diploma_url()}\n"
            text += f"<b>Ijtimoiy holati:</b> {applied_student.social_status}\n"
            text += f"<b>Ijtimoiy holat fayli:</b> \nhttps://camuf.uz/{applied_student.get_social_status_file_url()}\n"
            text += f"<b>Telefon raqami:</b> {applied_student.phone_number}\n"
            text += f"<b>Email:</b> {applied_student.email}\n"

            bot_request("sendMessage", {
                "chat_id": -1001566478762,
                'parse_mode': 'html',
                "text": text
            })
            stepHandler(user, message)

        elif user.user_step == 'get_lang':
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
            if "contact" not in message.keys():
                stepHandler(user, message)
            else:
                user.user_contact = message['contact']['phone_number']
                user.user_step = ''
                user.save()
                stepHandler(user, message)


def stepHandler(user, message):
    if user.user_step == "get_admission_name":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(user=user, text='iltimos ismizni kiriting'),
            "reply_markup": json.dumps({
                'remove_keyboard': True})
        })

    elif user.user_step == "get_admission_surname":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(user=user, text='iltimos famliyezni kiriting'),
            "reply_markup": json.dumps({
                'remove_keyboard': True})
        })

    elif user.user_step == "get_admission_fathers_name":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(user=user, text='iltimos otezni ismini kiriting'),
            "reply_markup": json.dumps({
                'remove_keyboard': True})
        })

    elif user.user_step == "get_admission_passport_number":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(user=user, text='iltimos pasport raqamini kiriting'),
            "reply_markup": json.dumps({
                'remove_keyboard': True})
        })
        
    elif user.user_step == "get_admission_passport_pdf":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(user=user, text='iltimos pasport nusxasini joylang'),
            "reply_markup": json.dumps({
                'remove_keyboard': True})
        })
        

    elif user.user_step == "get_admission_schooling_file":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(user=user, text="iltimos tamomlagan bilim yurtini tastiqlovchi xujjatni jo'nating"),
            "reply_markup": json.dumps({
                'remove_keyboard': True})
        })
    elif user.user_step == "get_admission_social_status_file":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(user=user, text="iltimos ijtimoiy xolatni tastiqlovchi xujjatni jo'nating"),
            "reply_markup": json.dumps({
                'remove_keyboard': True})
        })
    elif user.user_step == "get_admission_country":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(user=user, text='iltimos davlatizni kiriting'),
            "reply_markup": json.dumps({
                'keyboard': [[choice[1] for choice in COUNTRY_CHOICES_TELEGRAM]],
                'remove_keyboard': True})
        })

    elif user.user_step == "get_admission_region":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(user=user, text='iltimos viloyatni kiriting'),
            "reply_markup": json.dumps({
                'remove_keyboard': True})
        })
    
    elif user.user_step == "get_admission_district":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(user=user, text='iltimos tumanni kiriting'),
            "reply_markup": json.dumps({
                'remove_keyboard': True})
        })

    elif user.user_step == "get_admission_schooling":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(user=user, text='iltimos bitirgan bilim yurtini kiriting'),
             "reply_markup": json.dumps({
                'keyboard': [[choice[1] for choice in SCHOOL_CHOICES[1:]]],
                'resize_keyboard': True
                })
        })


    elif user.user_step == "get_admission_social_status":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(message=message, text='iltimos ijtimoiy holatni kiriting'),
            "reply_markup": json.dumps({
                'keyboard': [[choice[1] for choice in SOCIAL_STATUS[1:]]],
                'resize_keyboard': True
            })
        })

    elif user.user_step == "get_admission_phone_number":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(user=user, text='iltimos tel nomerni kiriting'),
            "reply_markup": json.dumps({
                'remove_keyboard': True})
        })

    elif user.user_step == "get_lang":
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
            'text': translate(user=user, text='iltimos username izni kiriting'),
            "reply_markup": json.dumps({
                'remove_keyboard': True})
        })
    elif user.user_step == "get_contact":
        bot_request("sendMessage", {
            "chat_id": user.user_id,
            'text': translate(user=user, text="contactni kiriting"),
            "reply_markup": json.dumps({
                "keyboard": [[{
                    'text': translate(user=user, text="contact"),
                    'request_contact': True
                }]],
                'remove_keyboard': True
            })
        })
    else:
        redirectToHomePage(message)



def redirectToHomePage(message, admin=False):
    user_id = message['from']['id']
    if admin:
        keyboard = [
                    [
                        translate(message=message, text="apply to uni"), translate(message=message, text='setting')
                    ], [
                        translate(message=message, text='biz haqimizda'), translate(message=message, text='statistika')
                    ]
                ]
    else:
        keyboard = [
                    [
                        translate(message=message, text="apply to uni"), translate(message=message, text='setting')
                    ], [
                        translate(message=message, text='biz haqimizda')
                    ]
                ]
    bot_request("sendMessage", {
        "chat_id": user_id,
        'text': translate(message=message, text="home page"),
        "reply_markup": json.dumps({
            "keyboard": keyboard,
            'resize_keyboard': True
        })
    })


def settingHandler(message):
    user_id = message['from']['id']
    userModel = BotUsers.objects.get(user_id=user_id)
    muloqot_tili = translate(text="O'zbekcha", message=message) if userModel.user_lang == 'uz' else translate(message=message, text='English')
    text = f"<b>{translate(text='Muloqot tili', message=message)}:</b> {muloqot_tili}\n" \
           f"<b>{translate(text='phone', message=message)}:</b> {userModel.user_contact}\n\n" \
           f'{translate(text="quyidagilardan birini tanlang", message=message)}'

    bot_request('sendMessage', {
        'chat_id': user_id,
        'parse_mode': 'html',
        'text': text,
        'reply_markup': json.dumps(
            {
                "inline_keyboard": [
                    [
                        {'text': translate(text="Til", message=message), 'callback_data': 'tilni_ozgartir'},
                        {'text': translate(text="contact", message=message), 'callback_data': 'nomerni_ozgartir'}
                    ]
                ]
            }
        )
    }
                )
    




def callbackHandler(message):
    if message['data']:
        user = BotUsers.objects.get(user_id=message['from']['id'])
        if user.user_step:
            setHandler(message, user)
        # admission_

        elif "all" in message['data'] and '/' in message['data']:
            program = message['data'].split("/")[1]
            export_and_send_application_info(message, "all", program)
        elif "today" in message['data'] and '/' in message['data']:
            program = message['data'].split("/")[1]
            export_and_send_application_info(message, "today", program)
        elif "last_week" in message['data'] and '/' in message['data']:
            program = message['data'].split("/")[1]
            export_and_send_application_info(message, "last_week", program)

        elif message['data'].split("_")[0] == 'admission':
            message_id = message['message']['message_id']
            delete_message(user.user_id, message_id)
            apply_to_uni(message)
        elif message['data'] == 'ozbekchaga_ozgartir' or message['data'] == 'inglizchaga_ozgartir':
            changeSettingHandler(message)

        elif message['data'] == 'tilni_ozgartir' or message['data'] == 'nomerni_ozgartir':
            changeSettingHandler(message)

     


def changeSettingHandler(message):
    user_id = message['from']['id']
    message_id = message['message']['message_id']
    userModel = BotUsers.objects.get(user_id=user_id)
    if message['data'] == 'tilni_ozgartir':
        bot_request('editMessageReplyMarkup', {
            'chat_id': user_id,
            'message_id': message_id,
            'parse_mode': 'html',
            'text': translate(text='tilni tanlang', message=message),
            'reply_markup': json.dumps(
                {
                    "inline_keyboard": [
                        [
                            {'text': translate(text="O'zbekcha", message=message), 'callback_data': 'ozbekchaga_ozgartir'},
                            {'text': translate(text="English", message=message), 'callback_data': 'inglizchaga_ozgartir'}
                        ]
                    ]
                }
            )
        }
                    )
    elif message['data'] == "nomerni_ozgartir":
        delete_message(user_id, message_id)

        userModel.user_step = 'get_contact'
        userModel.save()
        setHandler(message, userModel)

    elif message['data'] == 'ozbekchaga_ozgartir':
        delete_message(user_id, message_id)
        userModel.user_lang = 'uz'
        userModel.save()
        redirectToHomePage(message)
    elif message['data'] == 'inglizchaga_ozgartir':
        delete_message(user_id, message_id)
        userModel.user_lang = 'en'
        userModel.save()
        redirectToHomePage(message)


def delete_message(chat_id, message_id):
    bot_request('deleteMessage', {
        'chat_id': chat_id,
        'message_id': message_id
    })



def contactHandler(message):
    user_id = message['from']['id']
    user = BotUsers.objects.get(user_id=user_id)
    if user.user_step == "get_contact":
        user.phone = message['contact']['phone_number']
        user.user_step = ''
        user.save()
        redirectToHomePage(message)




def admissionHandler(message):
    user_id = message['from']['id']
    courses = UndergraduateCourse.objects.all()

    keyboards = [{'text': translate(text=f"{i.title}", message=message), 'callback_data': f"admission_{i.id}"} for i in courses]
    bot_request('sendPhoto', {
        'chat_id': user_id,
        'parse_mode': 'html',
        "photo": 'https://camuf.uz/static/images/logo.png',
        'caption': translate(message=message, text="admission_text"),
        'reply_markup': json.dumps(
            {
                "inline_keyboard": [
                    keyboards
                ]
            }
        )
    })

def apply_to_uni(message):
    user_id = message['from']['id']
    course_id = message['data'].split("_")[1]
    userModel = BotUsers.objects.get(user_id=user_id)

    try:
        selected_course = UndergraduateCourse.objects.get(id=course_id)
        try:
            student = AppliedStudents.objects.get(bot_id=userModel.user_id)
            student.program = selected_course
            student.save()
        except ObjectDoesNotExist:
            student = AppliedStudents.objects.create(program=selected_course, bot_id=userModel.user_id)

        userModel.user_step = "get_admission_name"
        userModel.save()

        stepHandler(userModel, message)

    except ObjectDoesNotExist:
        redirectToHomePage(message)



def handlePdffiles(message, file_type):
    file_id = message['document']['file_id']
    user_id = message['from']['id']
    applied_students = AppliedStudents.objects.get(bot_id=user_id)

    if file_type == "get_admission_country":
        get_file_path_save(file_id=file_id, file_type=applied_students.passport_pdf)
    elif file_type == "schooling_file":
        get_file_path_save(file_id=file_id, file_type=applied_students.diploma)
    elif file_type == "social_status_file":
        get_file_path_save(file_id=file_id, file_type=applied_students.social_status_file)
    applied_students.save()



def get_file_path_save(file_id, file_type):
    res = requests.get(f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}").json()
    file_path = f"https://api.telegram.org/file/bot{TOKEN}/{res['result']['file_path']}"
    download_and_save_file(file_path, file_type)
    

def download_and_save_file(url, file_field):
    response = urllib.request.urlopen(url)
    file_name = url.split('/')[-1]
    file_field.save(file_name, File(response))


def export_and_send_application_info(message, option, program, all_in_one=False):
    # Send the Excel file to the Telegram bot using the bot_request function
    message_id = message['message']['message_id']
    user_id = message['from']['id']
    delete_message(user_id, message_id)
    
    try:
        course = UndergraduateCourse.objects.get(title=program)
    except ObjectDoesNotExist:
        course = None

    today = datetime.date.today()
    last_week = today - datetime.timedelta(days=7)
    if all_in_one:
        if option == 'today':
            applications = AppliedStudents.objects.filter(date_created__date=today)
        elif option == 'last_week':
            applications = AppliedStudents.objects.filter(date_created__date__gte=last_week, date_created__date__lte=today)
        elif option == 'all':
            applications = AppliedStudents.objects.all()
        else:
            print("Invalid option.")
            return
    else:
        if option == 'today':
            applications = course.program.filter(date_created__date=today)
        elif option == 'last_week':
            applications = course.program.filter(date_created__date__gte=last_week, date_created__date__lte=today)
        elif option == 'all':
            applications = course.program.all()
        else:
            print("Invalid option.")
            return       
    if applications.count() > 0:
        # Convert the queryset to a Pandas DataFrame
        df = pd.DataFrame(list(applications.values()))
        # Convert datetime fields to timezone-unaware
        df['date_created'] = df['date_created'].apply(make_naive)

        # Export DataFrame to Excel
        excel_file_path = f"static/statistics/{user_id}_application_info.xlsx"
        df.to_excel(excel_file_path, index=False)

        file_url = f"{BASE_DOMAIN}static/statistics/{user_id}_application_info.xlsx"

        send_file_from_url(file_url, user_id)

        # Remove the temporary Excel file
        os.remove(excel_file_path)
    else:
        bot_request("sendMessage", {
            "chat_id": user_id,
            "text": translate(message=message, text="hali hech narsa yo'q")
        })
    redirectToHomePage(message=message, admin=True)

def send_file_from_url(file_url, chat_id):
    bot_api_method = "sendDocument"
    bot_api_url = f"https://api.telegram.org/bot{TOKEN}/{bot_api_method}"

    # Download the file from the URL
    response = requests.get(file_url)

    if response.status_code == 200:
        # Extract the filename from the URL
        file_name = file_url.split("/")[-1]

        # Prepare the request data with the downloaded file
        files = {"document": (file_name, response.content)}
        data = {"chat_id": chat_id}

        response = requests.post(bot_api_url, files=files, data=data)

        if response.status_code == 200:
            print("File sent successfully!")
        else:
            print("Failed to send the file.")
    else:
        print("Failed to download the file.")





