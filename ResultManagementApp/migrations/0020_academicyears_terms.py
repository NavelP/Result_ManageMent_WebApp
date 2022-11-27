# Generated by Django 3.1.4 on 2022-11-26 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResultManagementApp', '0019_auto_20221126_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicYears',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year_1', models.CharField(max_length=30)),
                ('year_2', models.CharField(max_length=30)),
                ('year_3', models.CharField(max_length=30)),
                ('year_4', models.CharField(max_length=30)),
                ('year_5', models.CharField(max_length=30)),
                ('year_6', models.CharField(max_length=30)),
                ('year_7', models.CharField(max_length=30)),
                ('year_8', models.CharField(max_length=30)),
                ('year_9', models.CharField(max_length=30)),
                ('year_10', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('term_1', models.CharField(max_length=30)),
                ('term_2', models.CharField(max_length=30)),
                ('term_3', models.CharField(max_length=30)),
                ('term_4', models.CharField(max_length=30)),
            ],
        ),
    ]