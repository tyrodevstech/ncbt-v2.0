# Generated by Django 4.2.6 on 2023-10-24 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('std_portal', '0011_alter_enroll_options_alter_financialcollege_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistrationcollage',
            name='dob',
            field=models.DateField(null=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='studentregistrationuni',
            name='dob',
            field=models.DateField(null=True, verbose_name='date of birth'),
        ),
    ]
