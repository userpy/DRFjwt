# Generated by Django 3.0.5 on 2020-05-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutApp', '0005_auto_20200525_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
