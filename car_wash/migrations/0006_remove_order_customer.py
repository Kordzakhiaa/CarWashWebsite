# Generated by Django 3.1.6 on 2021-02-17 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_wash', '0005_auto_20210217_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
    ]
