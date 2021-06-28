from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, UpdateView

from adminka.models import *
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, UpdateUserForm


class HomePageView(TemplateView):
    template_name = 'main_page.html'


class FilmListView(ListView):
    model = Film
    template_name = 'main_page.html'
    paginate_by = 10
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['soon'] = Film.objects.filter(status="soon")
        context['show'] = Film.objects.filter(status="in_show")
        context['main_page'] = MainPage.objects.get(id=1)
        return context


class ProfileRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


class UpdateProfileView(UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = "profile.html"
