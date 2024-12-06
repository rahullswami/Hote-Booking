# Generated by Django 5.1.3 on 2024-12-04 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('destination', models.CharField(max_length=300)),
                ('message', models.TextField()),
            ],
        ),
    ]
