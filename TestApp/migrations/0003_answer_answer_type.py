# Generated by Django 3.0.5 on 2020-05-07 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0002_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_type',
            field=models.BooleanField(choices=[('Не варный', False), ('Верный', True)], default=False, verbose_name='Истинность'),
        ),
    ]
