# Generated by Django 3.0.5 on 2020-05-07 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0003_answer_answer_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='track',
            unique_together={('album',)},
        ),
    ]
