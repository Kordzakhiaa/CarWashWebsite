# Generated by Django 3.1.5 on 2021-01-28 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_wash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='car',
            field=models.OneToOneField(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='car_wash.car'),
        ),
    ]
