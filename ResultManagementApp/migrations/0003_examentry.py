# Generated by Django 3.1.4 on 2022-11-23 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResultManagementApp', '0002_department_faculty_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('cat_one', models.IntegerField()),
                ('cat_two', models.IntegerField()),
                ('main_exam', models.IntegerField()),
            ],
        ),
    ]
