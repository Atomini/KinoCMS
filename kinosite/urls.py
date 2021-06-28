from django.urls import path
from .views import *

urlpatterns = [

    path('', FilmListView.as_view(), name="home"),
    path('register/', ProfileRegisterView.as_view(), name="register"),
    path("profile/<slug:slug>", UpdateProfileView.as_view(), name="profile"),
    ]