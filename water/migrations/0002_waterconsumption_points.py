# Generated by Django 5.0.3 on 2024-03-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='waterconsumption',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
