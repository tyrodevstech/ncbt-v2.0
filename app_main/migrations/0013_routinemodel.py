# Generated by Django 4.2.6 on 2023-10-21 03:48

import app_main.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0012_coursemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoutineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('routine', models.FileField(null=True, upload_to=app_main.models.routine_upload_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_main.coursemodel')),
            ],
            options={
                'verbose_name': 'Course Routine',
                'verbose_name_plural': 'Course Routines',
            },
        ),
    ]
