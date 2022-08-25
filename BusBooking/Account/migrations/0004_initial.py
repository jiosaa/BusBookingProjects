# Generated by Django 4.0.6 on 2022-08-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0003_delete_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('full_name', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=200, null=True, unique=True)),
                ('phone_number', models.CharField(max_length=255, null=True, unique=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_routeadmin', models.BooleanField(default=False)),
                ('is_busadmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]