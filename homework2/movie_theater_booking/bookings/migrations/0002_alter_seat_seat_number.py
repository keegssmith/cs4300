# Generated by Django 4.2.11 on 2025-03-02 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat_number',
            field=models.CharField(max_length=10),
        ),
    ]
