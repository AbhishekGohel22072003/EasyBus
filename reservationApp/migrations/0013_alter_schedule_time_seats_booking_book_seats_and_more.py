# Generated by Django 5.0.4 on 2024-04-30 15:50

import datetime
import django.db.models.expressions
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservationApp', '0012_alter_schedule_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.TimeField(default=datetime.time),
        ),
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeStamp', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(default=None, null=True, on_delete=django.db.models.expressions.Case, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='book_seats',
            field=models.ManyToManyField(related_name='book_seats', to='reservationApp.seats'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='seats',
            field=models.ManyToManyField(related_name='seats', to='reservationApp.seats'),
        ),
    ]
