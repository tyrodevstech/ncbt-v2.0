# Generated by Django 4.2.6 on 2023-10-17 06:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0006_countermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FounderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(null=True, upload_to='founder-profile-image', verbose_name='profile image')),
                ('founder_details', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
            ],
            options={
                'verbose_name': 'Founder',
                'verbose_name_plural': 'Founder Details',
            },
        ),
    ]
