from curses.ascii import HT
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import ContactForm
from app.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.utils import translation
from django.http import HttpResponseRedirect
from django.db.models import Q
import requests
from itertools import chain
from .credentials import URL
# Create your views here.


def index(request):
    news = New.objects.all()
    events = Event.objects.all()
    try:
        status = Status.objects.get(id=1)
    except:
        status = None

    context = {"news": news, "status": status, "events": events}
    return render(request, "index.html", context)


def about(request):
    try:
        status = Status.objects.get(id=1)
    except ObjectDoesNotExist:
        status = None

    context = {"status": status}
    return render(request, "about-us.html", context)


def contact(request):
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

    context = {"form": form}
    return render(request, "contacts.html", context)


def news(request):
    if request.method == "POST":
        search = request.POST['search']
        news = New.objects.filter(title__contains=search)
    else:
        news = New.objects.all()

    gallery = Gallery.objects.all().order_by('-id')[:10]

    news_catagory = NewsCatagory.objects.all()
    context = {"news": news, "gallery": gallery,
               'news_catagory': news_catagory}
    return render(request, "grid-news.html", context)


def news_search(request, **kwarg):
    search = kwarg['search']

    months = {'jan': 1, 'feb': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
              'july': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
    
    if search in months.keys():
        news = New.objects.filter(date_created__month=months[search])
    else:
        catagory = NewsCatagory.objects.get(slug=search)
        news = catagory.new_set.all()

    gallery = Gallery.objects.all().order_by('-id')[:10]
    news_catagory = NewsCatagory.objects.all()
    context = {"news": news, "gallery": gallery,
               'news_catagory': news_catagory}
    return render(request, "grid-news.html", context)


def news_details(request, slug):
    try:
        news = New.objects.get(slug=slug)
    except ObjectDoesNotExist:
        news = None
    gallery = Gallery.objects.all().order_by('-id')[:10]
    news_catagory = NewsCatagory.objects.all()

    context = {"news": news, "gallery": gallery,
               'news_catagory': news_catagory}
    return render(request, "news-post-page.html", context)


def courses(request):
    url = request.path.split('/')
    if 'undergraduate' in url:
        courses = UndergraduateCourse.objects.all()
    elif "graduate" in url:
        courses = GraduateCourse.objects.all()
    else:
        courses = list(chain(UndergraduateCourse.objects.all(),
                       GraduateCourse.objects.all()))

    context = {"courses": courses}
    return render(request, "course-grid.html", context)


def course_details(request, **kwargs):
    slug = kwargs['slug']
    catagory = kwargs['catagory']
    if catagory == "undergraduate":
        course = UndergraduateCourse.objects.get(slug=slug)
    else:
        course = GraduateCourse.objects.get(slug=slug)
    context = {"course": course}
    return render(request, "course-details.html", context)


def gallery(request):
    gallery = Gallery.objects.all()

    context = {"gallery": gallery}
    return render(request, "gallery.html", context)


def history(request):
    return render(request, "history.html")


def events(request):
    events = Event.objects.all()

    context = {"events": events}
    return render(request, "events.html", context)


def event_details(request, slug):
    event = Event.objects.get(slug=slug)
    other_events = Event.objects.filter(~Q(slug=slug))
    context = {"event": event, "other_events": other_events}

    return render(request, "event-page.html", context)


def team(request):
    members = Workers.objects.all()

    context = {"members": members}
    return render(request, "team.html", context)


def leader(request):
    members = Leaders.objects.all()

    context = {"members": members}
    return render(request, "team.html", context)


def member_details(request, **kwargs):
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

    context = {"team_member": team_member}
    return render(request, "team-member-profile.html", context)


def search_result(request):
    return render(request, "search-results.html")


def save_email(request):
    if request.method == "POST":
        email = request.POST['email']
        interested_person = InterestedPeople.objects.get_or_create(
            saved_email=email)
    return redirect("home")


def change_lang(request):
    LANGUAGE_SESSION_KEY = '_language'
    if request.method == "POST":
        sent_url = request.POST['next']
        old_lang = request.LANGUAGE_CODE
        changed_lang = request.POST['language']
        translation.activate(changed_lang)
        request.session[LANGUAGE_SESSION_KEY] = changed_lang
        url_details = sent_url.split('/')[1:-1]

        # # I use HTTP_REFERER to direct them back to previous path
        if "en/" in sent_url:
            if changed_lang != 'uz':
                new_url = sent_url[0:4].replace('en', changed_lang)
                if len(url_details) > 2:
                    new_url += url_details[1] + "/" + url_details[2] + "/"
                elif len(url_details) > 1:
                    new_url += url_details[1] + "/"

                return HttpResponseRedirect(new_url)
            elif changed_lang == 'uz':
                new_url1 = sent_url[0:4].replace('en', '')
                new_url = new_url1[1:]
                if len(url_details) > 2:
                    new_url += url_details[1] + "/" + url_details[2] + "/"
                elif len(url_details) > 1:
                    new_url += url_details[1] + "/"
                return HttpResponseRedirect(new_url)
        elif "ru/" in sent_url:
            if changed_lang != 'uz':
                new_url = sent_url[0:4].replace('ru', changed_lang)
                if len(url_details) > 2:
                    new_url += url_details[1] + "/" + url_details[2] + "/"
                elif len(url_details) > 1:
                    new_url += url_details[1] + "/"
                return HttpResponseRedirect(new_url)
            elif changed_lang == 'uz':
                new_url1 = sent_url[0:4].replace('ru', '')
                new_url = new_url1[1:]
                if len(url_details) > 2:
                    new_url += url_details[1] + "/" + url_details[2] + "/"
                elif len(url_details) > 1:
                    new_url += url_details[1] + "/"
                return HttpResponseRedirect(new_url)
        elif old_lang == "uz" and changed_lang != 'uz':
            new_url = f"/{changed_lang}" + sent_url

            return HttpResponseRedirect(new_url)

        return HttpResponseRedirect(sent_url)


def bot_request(method, data):
    requests.post(URL + method, data)
    # https://api.telegram.org/bot5838898419:AAETJYe3S96ZeMRFNv6MzkfsTDdrNu-3Qts/sendMessage?chat_id=-1001566478762&text=salom
