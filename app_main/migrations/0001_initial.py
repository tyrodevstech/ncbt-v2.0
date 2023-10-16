# Generated by Django 4.2.6 on 2023-10-14 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122, null=True)),
                ('email', models.CharField(max_length=122, null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('address', models.CharField(blank=True, max_length=12, null=True)),
                ('desc', models.TextField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=150, null=True)),
                ('post_content', models.TextField(max_length=500, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NoticeImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('notice_images', models.ImageField(blank=True, null=True, upload_to='notice_images')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Image Notice',
                'verbose_name_plural': 'Image Notice',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122, null=True)),
                ('post', models.CharField(max_length=120, null=True)),
                ('educational_qualification', models.CharField(max_length=255, null=True)),
                ('teacher_picture', models.ImageField(blank=True, null=True, upload_to='teacher_picture')),
            ],
        ),
    ]