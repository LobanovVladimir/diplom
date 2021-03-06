# Generated by Django 4.0.4 on 2022-05-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_users_password2'),
    ]

    operations = [
        migrations.CreateModel(
            name='places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=20)),
                ('longtitude', models.DecimalField(decimal_places=3, max_digits=20)),
                ('usersname', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
    ]
