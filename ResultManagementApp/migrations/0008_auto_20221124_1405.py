# Generated by Django 3.1.4 on 2022-11-24 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ResultManagementApp', '0007_academicyear_term_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicyear',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='academic_year',
            field=models.ForeignKey(default=2022, on_delete=django.db.models.deletion.CASCADE, to='ResultManagementApp.academicyear'),
            preserve_default=False,
        ),
    ]
