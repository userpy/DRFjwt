# Generated by Django 3.0.5 on 2020-05-11 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0015_answer_user_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='user_answer',
        ),
    ]
