# Generated by Django 4.2.3 on 2023-07-19 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_alter_masterpackage_timeline'),
    ]

    operations = [
        migrations.AddField(
            model_name='mastertimeline',
            name='status',
            field=models.IntegerField(choices=[(1, 'Activated'), (2, 'Deactivated')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='masterpackage',
            name='timeline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='package_related', to='exam.mastertimeline'),
        ),
        migrations.AlterField(
            model_name='mastertimeline',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='timeline_related', to='exam.masteryear'),
        ),
    ]