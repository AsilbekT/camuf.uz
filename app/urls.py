from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('journals/', views.journals, name="journals"),
    path('gallery/', views.gallery, name="gallery"),
    path('admission/', views.admission, name="admission"),
    path('admission/apply/', views.apply_form, name="apply_form"),
    path('success/', views.success, name="success"),
    path('contact/', views.contact, name="contact"),
    path('save_email/', views.save_email, name="save_email"),

    path('news/', views.news, name="news"),
    path('news/search?q=<str:search>&k=<str:model>/', views.data_search, name="data_search"),
    path('news/<slug:slug>/', views.news_details, name="news_details"),

    path('articles/', views.articles, name="articles"),
    path('articles/<slug:slug>/', views.article_details, name="article_details"),

    path('courses/', views.courses, name="courses"),
    path('courses/undergraduate/', views.courses, name="undergraduate"),
    path('courses/graduate/', views.courses, name="graduate"),
    path('courses/<str:catagory>/<slug:slug>/',
         views.course_details, name="course_details"),
    path('gallery/', views.gallery, name="gallery"),
    path('history/', views.history, name="history"),
    path('events/', views.events, name="events"),
    path('events/<slug:slug>/', views.event_details, name="event_details"),
    path('team/', views.team, name="team"),
    path('leaders/', views.leader, name="leaders"),
    path('team/<str:catagory>/<slug:slug>/',
         views.member_details, name="member_details"),
    path('search_result/', views.search_result, name="search_result"),
    path("change_lang/", views.change_lang, name="change_lang"),
]
