# Generated by Django 3.2.4 on 2021-06-27 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0006_news_promo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_link',
            field=models.URLField(verbose_name='Ссылка на видео'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название новости'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_link',
            field=models.URLField(verbose_name='Ссылка видео'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='promo_name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название акции'),
        ),
    ]
