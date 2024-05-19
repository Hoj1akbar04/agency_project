# Generated by Django 5.0.3 on 2024-05-19 12:09

import django.db.models.deletion
import users.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=users.helpers.SaveMediaFile.travel_image)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('comments', models.ManyToManyField(blank=True, to='users.comments')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.country')),
            ],
        ),
    ]