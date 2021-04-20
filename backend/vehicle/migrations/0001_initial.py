# Generated by Django 2.2.19 on 2021-04-20 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taxi_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.URLField()),
                ('base_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_description', models.CharField(max_length=255)),
                ('plate_number', models.CharField(max_length=10)),
                ('timestamp_registered', models.DateTimeField(auto_now_add=True)),
                ('is_on_duty', models.BooleanField(blank=True, null=True)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_driver', to='taxi_profile.DriverProfile')),
                ('vehicle_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_vehicle_type', to='vehicle.VehicleType')),
            ],
        ),
    ]
