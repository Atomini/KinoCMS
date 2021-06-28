from django.db import models
from ckeditor.fields import RichTextField
from pytils.translit import slugify
from django.utils import timezone


class MainPage(models.Model):

    phone_1 = models.CharField("Телефон №1", blank=False, max_length=15)
    phone_2 = models.CharField("Телефон №2", blank=True, max_length=15)
    SEO_text = RichTextField("SEO Text", blank=False)
    SEO_url = models.URLField("URL: ", blank=True)
    SEO_title = models.CharField("Title: ", max_length=255, blank=True)
    SEO_keywords = models.CharField("Keywords: ", max_length=255, blank=True)
    SEO_description = models.CharField("Description: ", max_length=255, blank=True)
    published_date = models.DateField("Дата публикации", blank=True, default=timezone.now)


class CinemaContact(models.Model):

    cinema_name = models.CharField("Название новости", max_length=255, blank=False, unique=True)
    address = RichTextField("Описание", blank=False)
    longitude = models.CharField("Долгота", blank=False, max_length=15)
    latitude = models.CharField("Широта", blank=False, max_length=15)
    cinema_logo = models.ImageField('Логотип', upload_to="image/cinema/", blank=False)
    status = models.BooleanField('Показать', default=True)



class ContactPage(models.Model):

    SEO_url = models.URLField("URL: ", blank=True)
    SEO_title = models.CharField("Title: ", max_length=255, blank=True)
    SEO_keywords = models.CharField("Keywords: ", max_length=255, blank=True)
    SEO_description = models.CharField("Description: ", max_length=255, blank=True)
    published_date = models.DateField("Дата публикации", blank=True, default=timezone.now)


class Pages(models.Model):

    page_name = models.CharField("Название", max_length=255, blank=False, unique=True)
    status = models.BooleanField('Показать', default=False)
    page_slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="Slug")
    page_descriptions = RichTextField("Описание", blank=False)
    page_main_image = models.ImageField('Главная картинка', upload_to="image/pages/", blank=False)
    image_1 = models.ImageField(upload_to="image/pages/", blank=True)
    image_2 = models.ImageField(upload_to="image/pages/", blank=True)
    image_3 = models.ImageField(upload_to="image/pages/", blank=True)
    image_4 = models.ImageField(upload_to="image/pages/", blank=True)
    image_5 = models.ImageField(upload_to="image/pages/", blank=True)
    published_date = models.DateField("Дата публикации", blank=True, default=timezone.now)

    SEO_url = models.URLField("URL: ", blank=True)
    SEO_title = models.CharField("Title: ", max_length=255, blank=True)
    SEO_keywords = models.CharField("Keywords: ", max_length=255, blank=True)
    SEO_description = models.CharField("Description: ", max_length=255, blank=True)

    # автоматически генерируем слаг при сохранении
    def save(self, *args, **kwargs):
        self.page_slug = slugify(self.page_name)
        super(Pages, self).save(*args, **kwargs)
