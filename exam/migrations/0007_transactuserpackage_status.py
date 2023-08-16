# Generated by Django 4.2.3 on 2023-08-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_transactuserpackage'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactuserpackage',
            name='status',
            field=models.IntegerField(choices=[(1, 'Ready'), (2, 'Done')], default=1),
            preserve_default=False,
        ),
    ]
