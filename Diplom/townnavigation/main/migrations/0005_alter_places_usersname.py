# Generated by Django 4.0.4 on 2022-05-22 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_places'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='usersname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.users'),
        ),
    ]
