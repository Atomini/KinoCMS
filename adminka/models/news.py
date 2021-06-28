from django.db import models
from django.utils import timezone
from pytils.translit import slugify  # успользуем вместо стпндартного иза использования кирилицы
from ckeditor.fields import RichTextField


class News(models.Model):

    news_name = models.CharField("Название новости", max_length=255, blank=False, unique=True)
    status = models.BooleanField('Показать', default=False)
    news_slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="Slug")
    news_descriptions = RichTextField("Описание", blank=False)
    news_main_image = models.ImageField('Главная картинка', upload_to="image/news/", blank=False)
    image_1 = models.ImageField(upload_to="image/news/", blank=True)
    image_2 = models.ImageField(upload_to="image/news/", blank=True)
    image_3 = models.ImageField(upload_to="image/news/", blank=True)
    image_4 = models.ImageField(upload_to="image/news/", blank=True)
    image_5 = models.ImageField(upload_to="image/news/", blank=True)
    news_link = models.URLField("Ссылка на видео", blank=True)
    published_date = models.DateField("Дата публикации", blank=True, default=timezone.now)
    SEO_url = models.URLField("URL: ", blank=True)
    SEO_title = models.CharField("Title: ", max_length=255, blank=True)
    SEO_keywords = models.CharField("Keywords: ", max_length=255, blank=True)
    SEO_description = models.CharField("Description: ", max_length=255, blank=True)

    # автоматически генерируем слаг при сохранении
    def save(self, *args, **kwargs):
        self.news_slug = slugify(self.news_name)
        super(News, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/admin/news/'
