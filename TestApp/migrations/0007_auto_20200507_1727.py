# Generated by Django 3.0.5 on 2020-05-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0006_auto_20200507_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_name',
            field=models.CharField(max_length=100, verbose_name='Название теста'),
        ),
    ]
