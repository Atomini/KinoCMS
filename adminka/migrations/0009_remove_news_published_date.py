# Generated by Django 3.2.4 on 2021-06-27 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0008_alter_news_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='published_date',
        ),
    ]
