# Generated by Django 3.2.9 on 2022-01-29 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summercamp', '0002_alter_contactus_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_description',
            name='summercamp_id',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='program_details',
            name='summercamp_id',
            field=models.CharField(max_length=20),
        ),
    ]