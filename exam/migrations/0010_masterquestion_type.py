# Generated by Django 4.2.3 on 2023-08-08 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_masteranswer_isright'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterquestion',
            name='type',
            field=models.IntegerField(choices=[(1, 'Multiple Choice'), (2, 'True False'), (3, 'Multiple Check')], default=1),
            preserve_default=False,
        ),
    ]
