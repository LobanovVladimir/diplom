# Generated by Django 4.0.4 on 2022-05-20 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_users_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='password2',
        ),
    ]
