# Generated by Django 3.1.5 on 2021-01-28 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_wash', '0002_auto_20210128_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='car',
        ),
        migrations.AddField(
            model_name='car',
            name='car_owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car_wash.customer'),
        ),
    ]
