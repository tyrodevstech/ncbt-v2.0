# Generated by Django 4.2.6 on 2023-10-16 06:56

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0003_alter_footerinformationmodel_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_banner', models.ImageField(null=True, upload_to='admission-banner')),
                ('admission_details', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
            ],
            options={
                'verbose_name': 'Admission',
                'verbose_name_plural': 'Admissions',
            },
        ),
        migrations.AlterField(
            model_name='contactinformationmodel',
            name='work',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Working Date & Time'),
        ),
    ]