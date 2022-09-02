# Generated by Django 4.0.6 on 2022-08-25 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('System_admin', '0001_initial'),
        ('Booker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travaler_name', models.CharField(max_length=255, null=True)),
                ('traveler_contact', models.CharField(max_length=255, null=True)),
                ('seat', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=255, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('bus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='System_admin.bus')),
                ('route', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Booker.route')),
            ],
        ),
    ]
