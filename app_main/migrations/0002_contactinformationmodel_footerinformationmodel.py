# Generated by Django 4.2.6 on 2023-10-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(blank=True, max_length=325, null=True, verbose_name='Short Summary')),
                ('phone', models.CharField(max_length=122, null=True)),
                ('email', models.CharField(max_length=122, null=True)),
                ('address', models.TextField(blank=True, max_length=325, null=True)),
                ('work', models.TextField(blank=True, max_length=325, null=True, verbose_name='Working Date & Time')),
            ],
            options={
                'verbose_name': 'Contact Information',
                'verbose_name_plural': 'Contact Informations',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='FooterInformationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(help_text='image size: w-250px x h-120', null=True, upload_to='footer_logo', verbose_name='Footer logo')),
                ('details', models.TextField(max_length=325, null=True, verbose_name='Short Summary')),
                ('facebook_link', models.URLField(blank=True, null=True, verbose_name='Facebook Link')),
                ('twitter_link', models.URLField(blank=True, null=True, verbose_name='Twitter Link')),
                ('instagram_link', models.URLField(blank=True, null=True, verbose_name='Instagram Link')),
                ('youtube_link', models.URLField(blank=True, null=True, verbose_name='YouTube Link')),
            ],
            options={
                'verbose_name': 'Footer Information',
                'verbose_name_plural': 'Footer Informations',
                'ordering': ['-id'],
            },
        ),
    ]
