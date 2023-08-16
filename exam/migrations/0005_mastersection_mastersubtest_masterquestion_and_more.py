# Generated by Django 4.2.3 on 2023-08-01 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_mastertimeline_activitydate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='section_related', to='exam.masterpackage')),
            ],
        ),
        migrations.CreateModel(
            name='MasterSubTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subtest_related', to='exam.mastersection')),
            ],
        ),
        migrations.CreateModel(
            name='MasterQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('subtest', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='question_related', to='exam.mastersubtest')),
            ],
        ),
        migrations.CreateModel(
            name='MasterAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answer_related', to='exam.masterquestion')),
            ],
        ),
    ]
