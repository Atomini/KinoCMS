from django.db import models
from django.utils import timezone
from pytils.translit import slugify  # успользуем вместо стпндартного иза использования кирилицы
from ckeditor.fields import RichTextField


class Promo(models.Model):

    promo_name = models.CharField("Название акции", max_length=255, blank=False, unique=True)
    status = models.BooleanField('Показать', default=False)
    promo_slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="Url")
    promo_descriptions = RichTextField("Описание", blank=False)
    promo_main_image = models.ImageField('Главная картинка', upload_to="image/promo/", blank=False)
    image_1 = models.ImageField(upload_to="image/promo/", blank=True)
    image_2 = models.ImageField(upload_to="image/promo/", blank=True)
    image_3 = models.ImageField(upload_to="image/promo/", blank=True)
    image_4 = models.ImageField(upload_to="image/promo/", blank=True)
    image_5 = models.ImageField(upload_to="image/promo/", blank=True)
    promo_link = models.URLField("Ссылка видео", blank=True)
    published_date = models.DateField("Дата публикации", blank=True, default=timezone.now)
    SEO_url = models.URLField("URL: ", blank=True)
    SEO_title = models.CharField("Title: ", max_length=255, blank=True)
    SEO_keywords = models.CharField("Keywords: ", max_length=255, blank=True)
    SEO_description = models.CharField("Description: ", max_length=255, blank=True)

    # автоматически генерируем слаг при сохранении
    def save(self, *args, **kwargs):
        self.promo_slug = slugify(self.promo_name)
        super(Promo, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/admin/promo/'

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"
