from django.db import models
from pytils.translit import slugify # успользуем вместо стпндартного иза использования кирилицы
from ckeditor.fields import RichTextField
# Create your models here.


class Film (models.Model):
    STATUS = [
        ('in_show', 'В показе'),
        ('soon', 'Скоро'),
        ('archive', 'Архив'),
    ]

    film_name = models.CharField("Название фильма", max_length=255, blank=False, unique=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="Url")
    film_descriptions = RichTextField("Описание", blank=False)
    film_main_image = models.ImageField('Главная картинка', upload_to="image/film/", blank=False)
    image_1 = models.ImageField(upload_to="image/film/", blank=True)
    image_2 = models.ImageField(upload_to="image/film/", blank=True)
    image_3 = models.ImageField(upload_to="image/film/", blank=True)
    image_4 = models.ImageField(upload_to="image/film/", blank=True)
    image_5 = models.ImageField(upload_to="image/film/", blank=True)
    trailer_link = models.URLField("Ссылка на трейлер", blank=False)
    type_3D = models.BooleanField("3D", default=False)
    type_2D = models.BooleanField("2D", default=False)
    type_IMAX = models.BooleanField("IMAX", default=False)
    status = models.CharField("Статус", choices=STATUS, default='soon', max_length=10)
    SEO_url = models.URLField("URL: ", blank=True)
    SEO_title = models.CharField("Title: ", max_length=255, blank=True)
    SEO_keywords = models.CharField("Keywords: ", max_length=255, blank=True)
    SEO_description = models.CharField("Description: ", max_length=255, blank=True)

    # автоматически генерируем слаг при сохранении
    def save(self, *args, **kwargs):
        self.slug = slugify(self.film_name)
        super(Film, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/admin/film/'

