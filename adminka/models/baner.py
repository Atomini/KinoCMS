from django.db import models


class UpperBanner(models.Model):

    url = models.URLField("URL", blank=True)
    banner_text = models.CharField("Текст", blank=True, max_length=200)
    image = models.ImageField(upload_to="image/banner/", blank=True)


class TopBanner(models.Model):

    url = models.URLField("URL", blank=True)
    banner_text = models.CharField("Текст", blank=True, max_length=200)
    image = models.ImageField(upload_to="image/banner/", blank=True)


class EndToEnd(models.Model):

    image = models.ImageField(upload_to="image/banner/", blank=True)
    back_color = models.CharField("Просто фон", blank=True, max_length=20)


class PromotionBanner(models.Model):
    url = models.URLField("URL", blank=True)
    banner_text = models.CharField("Текст", blank=True, max_length=200)
    image = models.ImageField(upload_to="image/banner/", blank=True)


class BannerSetting(models.Model):

    enable_upper_banner = models.BooleanField('Показать', default=False)
    speed_upper_banner = models.IntegerField("Скорость вращения", default=5)
    enable_top_banner = models.BooleanField('Показать', default=False)
    speed_top_banner = models.IntegerField("Скорость вращения", default=5)
    enable_promotion_banner = models.BooleanField('Показать', default=False)
    speed_promotion_banner = models.IntegerField("Скорость вращения", default=5)