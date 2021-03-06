# Generated by Django 3.2.4 on 2021-06-26 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0002_film'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='status',
            field=models.CharField(choices=[('in_show', 'В показе'), ('soon', 'Скоро'), ('archive', 'Архив')], default='soon', max_length=10, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('rus', 'Русский'), ('ukr', 'Украинский')], default='rus', max_length=10, verbose_name='Язык'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский')], default='male', max_length=10, verbose_name='Пол'),
        ),
    ]
