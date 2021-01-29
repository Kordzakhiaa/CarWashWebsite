# Generated by Django 3.1.5 on 2021-01-29 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarWasher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_start_date', models.DateTimeField(verbose_name='Order Start Date')),
                ('order_end_date', models.DateTimeField(verbose_name='Order End Date')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Finished', 'Finished')], max_length=200, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_wash.customer')),
                ('washer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_wash.carwasher')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(choices=[('crossover', 'crossover'), ('sedan', 'sedan'), ('hatchback', 'hatchback')], max_length=200)),
                ('license_plate', models.CharField(max_length=30)),
                ('car_owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car_wash.customer')),
            ],
        ),
    ]
