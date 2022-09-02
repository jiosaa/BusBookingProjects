# Generated by Django 4.0.6 on 2022-09-01 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('System_admin', '0002_rename_bus_type_bus_about_remove_bus_bus_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('start', models.CharField(max_length=255, null=True)),
                ('destination', models.CharField(max_length=255, null=True)),
                ('via_cities', models.CharField(max_length=255, null=True)),
                ('travel_date', models.DateField(null=True)),
                ('travel_begin_time', models.TimeField(null=True)),
                ('travel_distance', models.IntegerField(null=True)),
                ('travel_aproximate_time', models.CharField(max_length=255, null=True)),
                ('single_seat_price', models.IntegerField(null=True)),
                ('travel_facilities', models.CharField(max_length=255, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('route_admin', models.ManyToManyField(related_name='route_admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Single_Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_number', models.CharField(max_length=200, null=True)),
                ('bus_type', models.CharField(max_length=200, null=True)),
                ('bus_detail', models.CharField(max_length=200, null=True)),
                ('number_of_seats', models.IntegerField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('bus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='System_admin.bus')),
            ],
        ),
        migrations.CreateModel(
            name='SubRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Bus_admin.single_bus')),
                ('main_route', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Bus_admin.route')),
            ],
        ),
        migrations.CreateModel(
            name='SubRouteBusAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subroute_bus', models.ManyToManyField(to='Bus_admin.single_bus')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubRouteAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_route', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Bus_admin.subroute')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
