# Generated by Django 3.1.4 on 2022-11-24 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResultManagementApp', '0015_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicyear',
            name='term',
        ),
    ]