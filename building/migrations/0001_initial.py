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
            name='Build',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=users.helpers.SaveMediaFile.home_image)),
                ('price', models.FloatField()),
                ('price_type', models.CharField(choices=[('USD', '$'), ('UZS', "SO'M")], default='USD', max_length=8)),
                ('area', models.FloatField()),
                ('beds', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('garages', models.IntegerField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.address')),
                ('agents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.agents')),
            ],
        ),
    ]
