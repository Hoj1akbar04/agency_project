# Generated by Django 5.0.3 on 2024-05-19 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='saw',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
