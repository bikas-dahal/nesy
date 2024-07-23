# Generated by Django 5.0.2 on 2024-07-23 03:49

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price_per_night', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('guests', models.IntegerField()),
                ('country', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='uploads/properties')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('favorited', models.ManyToManyField(blank=True, related_name='favorites', to='accounts.profile')),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('number_of_nights', models.IntegerField()),
                ('guests', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='accounts.profile')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='property.property')),
            ],
        ),
    ]
