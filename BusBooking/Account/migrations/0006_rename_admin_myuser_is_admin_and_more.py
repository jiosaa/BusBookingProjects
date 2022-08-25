# Generated by Django 4.0.6 on 2022-08-22 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_myuser_admin_myuser_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='admin',
            new_name='is_admin',
        ),
        migrations.RenameField(
            model_name='myuser',
            old_name='is_busadmin',
            new_name='is_staff',
        ),
        migrations.RenameField(
            model_name='myuser',
            old_name='is_routeadmin',
            new_name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='staff',
        ),
    ]