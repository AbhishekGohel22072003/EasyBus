# Generated by Django 5.0.4 on 2024-04-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservationApp', '0015_seats_booking_book_seats_schedule_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='seats',
            name='seat_number',
            field=models.IntegerField(default=0),
        ),
    ]
