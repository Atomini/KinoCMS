from django.db import models
from django.contrib.auth.models import AbstractUser
from pytils.translit import slugify # успользуем вместо стпндартного иза использования кирилицы
from django.utils import timezone


class User(AbstractUser):

    SEX = [
        ('male', 'Мужской'),
        ('female', 'Женский'),
    ]
    LANGUAGE = [
        ('rus', 'Русский'),
        ('ukr', 'Украинский'),
    ]
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="slug")
    address = models.CharField("Адресс", max_length=200, blank=True)
    card_num = models.CharField("Номер карты", max_length=16, blank=True)
    language = models.CharField("Язык", choices=LANGUAGE, default="rus", max_length=10)
    sex = models.CharField("Пол", choices=SEX, default='male', max_length=10)
    phone = models.CharField("Номер телефона", blank=True, max_length=100)
    birth_date = models.DateField("Дата рождения", blank=True, default=timezone.now)
    city = models.CharField('Город', max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/'