from curses.ascii import HT
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import ContactForm
from app.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.db.models import Q
import requests
from itertools import chain
from bot.credentials import URL
from .forms import AppliedStudentsForm
# Create your views here.


def index(request):
    news = New.objects.all()
    events = Event.objects.all()
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None

    context = {
        "news": news, 
        "status": status, 
        "events": events, 
        'phones': phones,
        'emails': emails
        }
    return render(request, "index.html", context)


def about(request):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None

    context = {"status": status, 
        'phones': phones,
        'emails': emails}
    return render(request, "about-us.html", context)


def contact(request):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = f"<b>Ism:</b> {data['firstname']}\n<b>Familiya</b>: {data['surname']}\n<b>Nomer</b>: {data['phone']}\n<b>Email</b>: {data['email']}\n<b>Xabar</b>: {data['message']}\n"

            bot_request("sendMessage", {
                "chat_id": -1001566478762,
                'parse_mode': 'html',
                "text": text
            })

            return redirect("home")
    else:
        form = ContactForm()

    context = {
        "form": form, 
        "status": status, 
        'phones': phones,
        'emails': emails
        }
    return render(request, "contacts.html", context)


def news(request):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None

    if request.method == "POST":
        search = request.POST['search']
        news = New.objects.filter(title__contains=search)
    else:
        news = New.objects.all()
    gallery = Gallery.objects.all().order_by('-id')[:10]


    catagories = NewsCatagory.objects.all()
    context = {
        "data": news, 
        "gallery": gallery,
        "status": status, 
        'catagories': catagories, 
        'phones': phones,
        'emails': emails
        }
    return render(request, "grid-news.html", context)


def data_search(request, **kwarg):
    search = kwarg['search']
    model = kwarg['model']

    months = {'jan': 1, 'feb': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
              'july': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None

    if search in months.keys():
        if model == "article":
            data = Article.objects.filter(date_created__month=months[search])
        else:
            data = New.objects.filter(date_created__month=months[search])
            print(data)
    else:
        if model == "article":
            try:
                catagory = ArticleCatagory.objects.get(slug=search)
                data = catagory.article_catagory.all()
            except ObjectDoesNotExist:
                catagory = None
                data = None
        else:
            try:
                catagory = NewsCatagory.objects.get(slug=search)
                data = catagory.news_catagory.all()
            except ObjectDoesNotExist:
                catagory = None
                data = None

    gallery = Gallery.objects.all().order_by('-id')[:10]

    if model == 'article':
        catagories = ArticleCatagory.objects.all()

        context = {
            "data": data, 
            "status": status, 
            "gallery": gallery,
            'catagories': catagories, 
            'phones': phones,
            'emails': emails
            }
        
        return render(request, "articles.html", context)

    
    catagories = NewsCatagory.objects.all()
    context = {
        "data": data, 
        "status": status, 
        "gallery": gallery,
        'catagories': catagories, 
        'phones': phones,
        'emails': emails
        }
    return render(request, "grid-news.html", context)





def news_details(request, slug):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None
    try:
        news = New.objects.get(slug=slug)
    except ObjectDoesNotExist:
        news = None
    gallery = Gallery.objects.all().order_by('-id')[:10]
    news_catagory = NewsCatagory.objects.all()

    context = {
        "news": news, 
        "gallery": gallery,
        "status": status, 
        'news_catagory': news_catagory, 
        'phones': phones,
        'emails': emails}
    return render(request, "news-post-page.html", context)


def courses(request):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None
    url = request.path.split('/')
    if 'undergraduate' in url:
        courses = UndergraduateCourse.objects.all()
    elif "graduate" in url:
        courses = GraduateCourse.objects.all()
    else:
        courses = list(chain(UndergraduateCourse.objects.all(),
                       GraduateCourse.objects.all()))

    context = {
        "courses": courses, 
        "status": status, 
        'phones': phones,
        'emails': emails
        }
    return render(request, "course-grid.html", context)


def course_details(request, **kwargs):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None
        
    slug = kwargs['slug']
    catagory = kwargs['catagory']
    if catagory == "undergraduate":
        course = UndergraduateCourse.objects.get(slug=slug)
    else:
        course = GraduateCourse.objects.get(slug=slug)
    context = {
        "course": course, 
        "status": status, 
        'phones': phones,
        'emails': emails
        }
    return render(request, "course-details.html", context)


def gallery(request):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None
    gallery = Gallery.objects.all()

    context = {"gallery": gallery, 
        'phones': phones,
        'emails': emails}
    return render(request, "gallery.html", context)


def articles(request):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None

    if request.method == "POST":
        search = request.POST['search']
        data = Article.objects.filter(title__contains=search)
    else:
        data = Article.objects.all()

    gallery = Gallery.objects.all().order_by('-id')[:10]

    catagories = ArticleCatagory.objects.all()
    context = {
        "data": data, 
        "status": status, 
        "gallery": gallery,
        'catagories': catagories, 
        'phones': phones,
        'emails': emails
        }
    return render(request, "articles.html", context)


def article_details(request, slug):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None
    try:
        data = Article.objects.get(slug=slug)
    except ObjectDoesNotExist:
        data = None
    gallery = Gallery.objects.all().order_by('-id')[:10]
    catagoryies = ArticleCatagory.objects.all()

    context = {
        "data": data, 
        "gallery": gallery,
        "status": status, 
        'catagoryies': catagoryies, 
        'phones': phones,
        'emails': emails
        }
    return render(request, "article_details.html", context)


def history(request):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None
    return render(request, "history.html")


def events(request):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None
    events = Event.objects.all()

    context = {
        "events": events, 
        "status": status, 
        'phones': phones,
        'emails': emails
        }
    return render(request, "events.html", context)


def event_details(request, slug):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None
    event = Event.objects.get(slug=slug)
    other_events = Event.objects.filter(~Q(slug=slug))
    context = {
        "event": event, 
        "status": status, 
        "other_events": other_events, 
        'phones': phones,
        'emails': emails
        }

    return render(request, "event-page.html", context)


def team(request):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None

    members = Workers.objects.all()

    context = {
        "members": members, 
        "status": status, 
        'phones': phones,
        'emails': emails
        }
    return render(request, "team.html", context)


def leader(request):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None

    members = Leaders.objects.all()

    context = {
        "members": members, 
        "status": status, 
        'phones': phones,
        'emails': emails
        }
    return render(request, "team.html", context)


def member_details(request, **kwargs):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None

    if kwargs['catagory'] == "staff":
        try:
            team_member = Workers.objects.get(slug=kwargs['slug'])
        except ObjectDoesNotExist:
            team_member = None
    else:
        try:
            team_member = Leaders.objects.get(slug=kwargs['slug'])
        except ObjectDoesNotExist:
            team_member = None

    context = {
        "team_member": team_member, 
        "status": status, 
        'phones': phones,
        'emails': emails
        }
    return render(request, "team-member-profile.html", context)


def search_result(request):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None

    return render(request, "search-results.html")


def save_email(request):
    if request.method == "POST":
        email = request.POST['email']
        interested_person = InterestedPeople.objects.get_or_create(
            saved_email=email)
    return redirect("home")


def change_lang(request):
    if request.method == "POST":
        next_url = request.POST.get('next', '/')
        old_lang = request.LANGUAGE_CODE
        changed_lang = request.POST.get('language')

        if changed_lang and changed_lang != old_lang:
            activate(changed_lang)
            request.session['_language'] = changed_lang
            url_parts = next_url.split('/')

            if changed_lang == 'ru':
                url_parts.pop(1)

            if old_lang == "ru" and changed_lang != "ru":
                url_parts.insert(1, changed_lang)

            if changed_lang in ['en', 'uz']:
                url_parts[1] = url_parts[1].replace(old_lang, changed_lang)

            new_url = '/'.join(url_parts)

            return redirect(new_url)

    return redirect(next_url)



def admission(request):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None
    gallery = UniversityGallery.objects.all()
    courses = UndergraduateCourse.objects.all()
    context = {
        "status": status, 
        'phones': phones,
        'emails': emails,
        'courses': courses,
        'gallery': gallery
        }
    return render(request, "yonalishlar.html", context)

def apply_form(request, slug):
    try:
        status = Status.objects.get(id=1)
        phones = status.phone_number.all()
        emails = status.university_email.all()
    except:
        status = None
    
    course = UndergraduateCourse.objects.get(slug=slug)

    if request.method == 'POST':
        form = AppliedStudentsForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save()
            instance.program = course
            instance.save()

            text = f"<b>Yangi arizachi</b>\n"
            text += f"<b>Yo'nalish:</b> {course.title}\n"
            text += f"<b>Familiyasi:</b> {form.cleaned_data['surname']}\n"
            text += f"<b>Ismi:</b> {form.cleaned_data['name']}\n"
            text += f"<b>Otasining ismi:</b> {form.cleaned_data['fathers_name']}\n"
            text += f"<b>Passport raqami:</b> {form.cleaned_data['passport_number']}\n"
            text += f"<b>Passport PDF:</b> \nhttps://camuf.uz{instance.get_passport_pdf_url()}\n"
            text += f"<b>Region:</b> {form.cleaned_data['region']}\n"
            text += f"<b>O'qish:</b> {form.cleaned_data['schooling']}\n"
            text += f"<b>Diplom raqami:</b> \nhttps://camuf.uz/{instance.get_diploma_url()}\n"
            text += f"<b>Ijtimoiy holati:</b> {form.cleaned_data['social_status']}\n"
            text += f"<b>Ijtimoiy holat fayli:</b> \nhttps://camuf.uz/{instance.get_social_status_file_url()}\n"
            text += f"<b>Telefon raqami:</b> {form.cleaned_data['phone_number']}\n"
            text += f"<b>Email:</b> {form.cleaned_data['email']}\n"

            bot_request("sendMessage", {
                "chat_id": -1001566478762,
                'parse_mode': 'html',
                "text": text
            })
            
            return redirect("success")


    else:
        form = AppliedStudentsForm()
    context = {
        "status": status, 
        'phones': phones,
        'emails': emails,
        'form': form,
        'slug': slug
        }
    return render(request, 'admission.html', context)


def success(request):
    return render(request, 'success.html')

def bot_request(method, data):
    requests.post(URL + method, data)
    # https://api.telegram.org/bot5838898419:AAETJYe3S96ZeMRFNv6MzkfsTDdrNu-3Qts/sendMessage?chat_id=-1001566478762&text=salom



