# Generated by Django 4.2.6 on 2023-10-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0004_admissionmodel_alter_contactinformationmodel_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderSliderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=125, null=True)),
                ('sub_title', models.TextField(blank=True, max_length=225, null=True)),
                ('btn_text', models.CharField(blank=True, max_length=20, null=True, verbose_name='button text')),
                ('btn_link', models.URLField(blank=True, null=True, verbose_name='button link')),
                ('bg_img', models.ImageField(help_text='image size: w-1920px x h-800', null=True, upload_to='header-sliders-bg', verbose_name='slider image')),
                ('active', models.BooleanField(default=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Header Slider',
                'verbose_name_plural': 'Header Sliders',
            },
        ),
    ]
