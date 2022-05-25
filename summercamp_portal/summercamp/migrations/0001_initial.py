# Generated by Django 4.0.1 on 2022-01-18 11:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cityevents',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('eventname', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('city', models.CharField(max_length=50)),
                ('venueaddress', models.TextField()),
                ('description', models.TextField()),
                ('eventpic', models.ImageField(default='', max_length=255, upload_to='summercamp/event_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45, null=True)),
                ('phone', models.IntegerField()),
                ('question', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('campname', models.CharField(max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('feedbacktext', models.TextField()),
                ('ratings', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('summercamp_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=45)),
                ('campname', models.CharField(max_length=50)),
                ('ownername', models.CharField(max_length=40)),
                ('campemailid', models.CharField(max_length=60)),
                ('campmobileno', models.IntegerField()),
                ('campaddress', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Program_details',
            fields=[
                ('program_id', models.AutoField(primary_key=True, serialize=False)),
                ('programname', models.CharField(max_length=100, null=True)),
                ('duration', models.CharField(max_length=20)),
                ('fees', models.CharField(max_length=30)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('description', models.TextField()),
                ('agegroup', models.CharField(max_length=15)),
                ('summercamp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summercamp.organizer')),
            ],
        ),
        migrations.CreateModel(
            name='Job_description',
            fields=[
                ('jobid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('postname', models.CharField(max_length=30)),
                ('noofseats', models.IntegerField()),
                ('lastdateofapply', models.DateField()),
                ('postdate', models.DateField()),
                ('description', models.TextField()),
                ('summercamp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summercamp.organizer')),
            ],
        ),
    ]