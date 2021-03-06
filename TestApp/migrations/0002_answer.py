# Generated by Django 3.0.5 on 2020-05-07 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='TestApp.Track')),
            ],
        ),
    ]
