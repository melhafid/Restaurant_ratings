# Generated by Django 4.0.6 on 2022-08-03 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('R_Restaurant_App', '0005_alter_restaurant_has_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='user',
        ),
    ]
