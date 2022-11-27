# Generated by Django 3.1.4 on 2022-11-24 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ResultManagementApp', '0017_delete_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ResultManagementApp.academicyear')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ResultManagementApp.course')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ResultManagementApp.term')),
            ],
        ),
    ]