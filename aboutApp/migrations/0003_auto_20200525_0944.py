# Generated by Django 3.0.5 on 2020-05-25 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutApp', '0002_auto_20200525_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_info',
            field=models.CharField(max_length=8000),
        ),
    ]
