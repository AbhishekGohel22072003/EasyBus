# Generated by Django 5.0.4 on 2024-04-30 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservationApp', '0018_alter_booking_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='fare',
            field=models.FloatField(default=0.0),
        ),
    ]
