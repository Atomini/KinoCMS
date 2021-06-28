# Generated by Django 3.2.4 on 2021-06-27 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0010_news_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Slug'),
        ),
    ]
