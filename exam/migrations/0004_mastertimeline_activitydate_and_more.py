# Generated by Django 4.2.3 on 2023-07-25 02:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_mastertimeline_status_alter_masterpackage_timeline_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mastertimeline',
            name='activitydate',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='mastertimeline',
            name='announcementdate',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='mastertimeline',
            name='liveclassdate',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='mastertimeline',
            name='registerdate',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
