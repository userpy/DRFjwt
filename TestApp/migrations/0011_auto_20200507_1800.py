# Generated by Django 3.0.5 on 2020-05-07 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0010_auto_20200507_1755'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set(),
        ),
    ]
