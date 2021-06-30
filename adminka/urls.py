from django.urls import path, include
from .views import *

urlpatterns = [
    path('film/addfilm/', AddFilmView.as_view(), name='addfilm'),
    path('film/', FilmListView.as_view(), name="film_view"),
    path("film/edit/<slug:slug>", UpdateFilmView.as_view(), name="film_update"),
    path("film/<slug:slug>/delete", DeleteFilmView.as_view(), name="film_delete"),

    path('statistic/', StatisticView.as_view(), name='statistic'),

    path("user/", UserListView.as_view(), name="user"),
    path("user/edit/<slug:slug>", UpdateUserView.as_view(), name="user_update"),
    path("user/add-user/", AddUserView.as_view(), name="adduser"),
    path("user/<slug:slug>/delete", DeleteUserView.as_view(), name="user_delete"),

    path('news/add-news/', AddNewsView.as_view(), name='addnews'),
    path('news/', NewsListView.as_view(), name='news_view'),
    path("news/edit/<slug:slug>", UpdateNewsView.as_view(), name="news_update"),
    path("news/<slug:slug>/delete", DeleteNewsView.as_view(), name="news_delete"),

    path('promo/add-promo/', AddPromoView.as_view(), name='addpromo'),
    path('promo/', PromoListView.as_view(), name='promo_view'),
    path("promo/edit/<slug:slug>", UpdatePromoView.as_view(), name="promo_update"),
    path("promo/<slug:slug>/delete", DeletePromoView.as_view(), name="promo_delete"),

    path('pages/', PageListView.as_view(), name='pages'),
    path('pages/edit/<pk>', UpdateMainPageView.as_view(), name='update_main_page'),
    path('banner/', banner_update, name='banner'),

    ]













