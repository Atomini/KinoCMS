# Generated by Django 3.2.4 on 2021-06-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0011_alter_news_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_link',
            field=models.URLField(blank=True, verbose_name='Ссылка на видео'),
        ),
    ]