from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import *
from .models import *
from django.shortcuts import render


# страница статистика
class StatisticView(TemplateView):
    template_name = 'statistic.html'


# Страница добавлени фильма
class AddFilmView(CreateView):
    model = Film
    form_class = AddFilmForm
    template_name = "admin/films/add_film.html"


# ------------------------Фильмы-------------------------
# Страница с фильмами
class FilmListView(ListView):
    model = Film
    template_name = "admin/films/film_list_view.html"
    paginate_by = 10
    allow_empty = False


# Редактирование фильма
class UpdateFilmView(UpdateView):
    model = Film
    form_class = UpdateFilmForm
    template_name = "admin/films/film_update_view.html"


class DeleteFilmView(DeleteView):
    model = Film
    template_name = "admin/films/film_delete_view.html"
    success_url = reverse_lazy("film_view")


# ---------------------------Пользователи---------------------------
class UserListView(ListView):
    model = User
    template_name = "admin/user/user_list_view.html"


class UpdateUserView(UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = "admin/user/user_update_view.html"
    success_url = reverse_lazy("user")


# Страница добавлени фильма
class AddUserView(CreateView):
    model = User
    form_class = AddUserForm
    template_name = "admin/user/add_user.html"
    success_url = reverse_lazy("user")


class DeleteUserView(DeleteView):
    model = User
    template_name = "admin/user/user_delete_view.html"
    success_url = reverse_lazy("user")


# -------------------------- Новости------------------------
# добавить новость
class AddNewsView(CreateView):
    model = News
    form_class = AddNewsForm
    template_name = "admin/news/add_news.html"
    success_url = reverse_lazy("news_view")


class NewsListView(ListView):
    model = News
    template_name = "admin/news/news_list_view.html"


class UpdateNewsView(UpdateView):
    model = News
    form_class = UpdateNewsForm
    template_name = "admin/news/news_update_view.html"
    success_url = reverse_lazy("news_view")
    slug_field = "news_slug"


class DeleteNewsView(DeleteView):
    model = News
    template_name = "admin/news/news_delete_view.html"
    success_url = reverse_lazy("news_view")
    slug_field = "news_slug"


# ---------------------------АКЦИИ --------------------------
class AddPromoView(CreateView):
    model = Promo
    form_class = AddPromoForm
    template_name = "admin/promo/add_promo.html"
    success_url = reverse_lazy("promo_view")


class PromoListView(ListView):
    model = Promo
    template_name = "admin/promo/promo_list_view.html"


class UpdatePromoView(UpdateView):
    model = Promo
    form_class = UpdatePromoForm
    template_name = "admin/promo/promo_update_view.html"
    success_url = reverse_lazy("promo_view")
    slug_field = "promo_slug"


class DeletePromoView(DeleteView):
    model = Promo
    template_name = "admin/promo/promo_delete_view.html"
    success_url = reverse_lazy("promo_view")
    slug_field = "promo_slug"


# ---------------------------Главная страница --------------------------
class UpdateMainPageView(UpdateView):
    model = MainPage
    form_class = UpdatePageForm
    template_name = "admin/page/main_page_update_view.html"
    success_url = reverse_lazy("pages")


class PageListView(ListView):
    model = Pages
    template_name = "admin/page/page_list_view.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page'] = MainPage.objects.get(id=1)
        return context


# ---------------------------Банеры --------------------------
def banner_view(request):

    if request.method == 'POST':  # If the form has been submitted...
        upper_banner_form = UpperBannerForm(request.POST, prefix="upper")
        top_banner_form = TopBannerForm(request.POST, prefix="top")
        end_form = EndToEndForm(request.POST, prefix="end")
        promotion_form = PromotionBannerForm(request.POST, prefix="promo")
        setting_form = BannerSettingForm(request.POST, prefix="setting")

        if upper_banner_form.is_valid() and top_banner_form.is_valid() and end_form.is_valid() and promotion_form.is_valid() and setting_form.is_valid():

            primary = upper_banner_form.save()
            top_banner_form.cleaned_data["top"] = primary
            b = top_banner_form.save()
            end_form.cleaned_data["end"] = primary
            c = end_form.save()
            promotion_form.cleaned_data["promo"] = primary
            d = promotion_form.save()
            setting_form.cleaned_data["setting"] = primary
            e = setting_form.save()

            return HttpResponseRedirect("/admin/banner/")


    else:
        upper_banner_form = UpperBannerForm(prefix="upper")
        top_banner_form = TopBannerForm(prefix="top")
        end_form = EndToEndForm(prefix="end")
        promotion_form = PromotionBannerForm(prefix="promo")
        setting_form = BannerSettingForm(prefix="setting")

        return render(request, 'admin/banner/banner.html', {
            'upper_form': upper_banner_form,
            'top_form': top_banner_form,
            'end_form': end_form,
            'promo_form': promotion_form,
            'setting_form': setting_form,
        })