# Generated by Django 3.2.4 on 2021-06-28 14:30

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0014_alter_news_news_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable_upper_banner', models.BooleanField(default=False, verbose_name='Показать')),
                ('speed_upper_banner', models.IntegerField(default=5, verbose_name='Скорость вращения')),
                ('enable_top_banner', models.BooleanField(default=False, verbose_name='Показать')),
                ('speed_top_banner', models.IntegerField(default=5, verbose_name='Скорость вращения')),
                ('enable_promotion_banner', models.BooleanField(default=False, verbose_name='Показать')),
                ('speed_promotion_banner', models.IntegerField(default=5, verbose_name='Скорость вращения')),
            ],
        ),
        migrations.CreateModel(
            name='CinemaContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinema_name', models.CharField(max_length=255, unique=True, verbose_name='Название новости')),
                ('address', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('longitude', models.CharField(max_length=15, verbose_name='Долгота')),
                ('latitude', models.CharField(max_length=15, verbose_name='Широта')),
                ('cinema_logo', models.ImageField(upload_to='image/cinema/', verbose_name='Логотип')),
                ('status', models.BooleanField(default=True, verbose_name='Показать')),
            ],
        ),
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SEO_url', models.URLField(blank=True, verbose_name='URL: ')),
                ('SEO_title', models.CharField(blank=True, max_length=255, verbose_name='Title: ')),
                ('SEO_keywords', models.CharField(blank=True, max_length=255, verbose_name='Keywords: ')),
                ('SEO_description', models.CharField(blank=True, max_length=255, verbose_name='Description: ')),
            ],
        ),
        migrations.CreateModel(
            name='EndToEnd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='image/banner/')),
                ('back_color', models.CharField(blank=True, max_length=20, verbose_name='Просто фон')),
            ],
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_1', models.CharField(max_length=15, verbose_name='Телефон №1')),
                ('phone_2', models.CharField(blank=True, max_length=15, verbose_name='Телефон №2')),
                ('SEO_text', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('SEO_url', models.URLField(blank=True, verbose_name='URL: ')),
                ('SEO_title', models.CharField(blank=True, max_length=255, verbose_name='Title: ')),
                ('SEO_keywords', models.CharField(blank=True, max_length=255, verbose_name='Keywords: ')),
                ('SEO_description', models.CharField(blank=True, max_length=255, verbose_name='Description: ')),
            ],
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('status', models.BooleanField(default=False, verbose_name='Показать')),
                ('page_slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('page_descriptions', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('page_main_image', models.ImageField(upload_to='image/pages/', verbose_name='Главная картинка')),
                ('image_1', models.ImageField(blank=True, upload_to='image/pages/')),
                ('image_2', models.ImageField(blank=True, upload_to='image/pages/')),
                ('image_3', models.ImageField(blank=True, upload_to='image/pages/')),
                ('image_4', models.ImageField(blank=True, upload_to='image/pages/')),
                ('image_5', models.ImageField(blank=True, upload_to='image/pages/')),
                ('SEO_url', models.URLField(blank=True, verbose_name='URL: ')),
                ('SEO_title', models.CharField(blank=True, max_length=255, verbose_name='Title: ')),
                ('SEO_keywords', models.CharField(blank=True, max_length=255, verbose_name='Keywords: ')),
                ('SEO_description', models.CharField(blank=True, max_length=255, verbose_name='Description: ')),
            ],
        ),
        migrations.CreateModel(
            name='PromotionBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, verbose_name='URL')),
                ('banner_text', models.CharField(blank=True, max_length=200, verbose_name='Текст')),
                ('image', models.ImageField(blank=True, upload_to='image/banner/')),
            ],
        ),
        migrations.CreateModel(
            name='TopBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, verbose_name='URL')),
                ('banner_text', models.CharField(blank=True, max_length=200, verbose_name='Текст')),
                ('image', models.ImageField(blank=True, upload_to='image/banner/')),
            ],
        ),
        migrations.CreateModel(
            name='UpperBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, verbose_name='URL')),
                ('banner_text', models.CharField(blank=True, max_length=200, verbose_name='Текст')),
                ('image', models.ImageField(blank=True, upload_to='image/banner/')),
            ],
        ),
    ]
