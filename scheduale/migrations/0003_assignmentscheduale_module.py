# Generated by Django 3.2 on 2022-07-02 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0001_initial'),
        ('scheduale', '0002_quizscheduale'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentscheduale',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='module.module'),
            preserve_default=False,
        ),
    ]