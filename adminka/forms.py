from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *


# Форма для бобавления фильма через админ панель
class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film

        fields = ["film_name", "film_descriptions", "film_main_image", "image_1", "image_2", "image_3", "image_4",
                  "image_5", 'trailer_link', "type_2D", "type_3D", "type_IMAX", "SEO_url", "SEO_title", "SEO_keywords",
                  "SEO_description", 'status']

        widgets = {
            "film_name": forms.TextInput(attrs={"type": "text", "class": "form-control",
                                                "placeholder": "Введите название фильма"}),

            "film_descriptions": forms.TextInput(attrs={"id": "summernote"}),
            "trailer_link": forms.URLInput(attrs={"class": "form-control", "placeholder": "Ссылка на видео в YouTube"}),
            "SEO_url": forms.URLInput(attrs={"class": "form-control", "placeholder": "URL"}),
            "SEO_title": forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Title"}),
            "SEO_keywords": forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "word"}),
            "SEO_description": forms.Textarea(attrs={"type": "text", "class": "form-control", "placeholder": "word"}),

        }


class UpdateFilmForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = "__all__"


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'address', 'card_num', 'language', 'sex', 'phone',
                  'is_staff', 'is_active', 'birth_date', 'city', 'last_login']


class AddUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'address', 'card_num', 'language', 'sex', 'phone',
                  'is_staff', 'is_active', 'birth_date', 'city']


class AddNewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['news_name', 'status', 'news_descriptions', 'news_main_image', 'image_1', 'image_2', 'image_3',
                  'image_4', 'image_5', 'news_link', 'published_date', 'SEO_url', 'SEO_title', 'SEO_keywords',
                  "SEO_description", ]


class AddPromoForm(forms.ModelForm):

    class Meta:
        model = Promo
        fields = ['promo_name', 'status', 'promo_descriptions', 'promo_main_image', 'image_1', 'image_2', 'image_3',
                  'image_4', 'image_5', 'promo_link', 'published_date', 'SEO_url', 'SEO_title', 'SEO_keywords',
                  "SEO_description", ]


class UpdateNewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['news_name', 'status', 'news_descriptions', 'news_main_image', 'image_1', 'image_2', 'image_3',
                  'image_4', 'image_5', 'news_link', 'published_date', 'SEO_url', 'SEO_title', 'SEO_keywords',
                  "SEO_description", 'news_slug', ]


class UpdatePromoForm(forms.ModelForm):

    class Meta:
        model = Promo
        fields = ['promo_name', 'status', 'promo_descriptions', 'promo_main_image', 'image_1', 'image_2', 'image_3',
                  'image_4', 'image_5', 'promo_link', 'published_date', 'SEO_url', 'SEO_title', 'SEO_keywords',
                  "SEO_description", 'promo_slug', ]


class UpdatePageForm(forms.ModelForm):

    class Meta:
        model = MainPage
        fields = "__all__"

# -----------------------Банеры -----------


class UpperBannerForm(forms.ModelForm):
    class Meta:
        model = UpperBanner
        fields = "__all__"


class TopBannerForm(forms.ModelForm):
    class Meta:
        model = TopBanner
        fields = "__all__"


class EndToEndForm(forms.ModelForm):
    class Meta:
        model = EndToEnd
        fields = "__all__"


class PromotionBannerForm(forms.ModelForm):
    class Meta:
        model = PromotionBanner
        fields = "__all__"


class BannerSettingForm(forms.ModelForm):
    class Meta:
        model = BannerSetting
        fields = "__all__"
