# Generated by Django 3.2 on 2022-07-02 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_auto_20220629_1237'),
        ('quiz', '0001_initial'),
        ('scheduale', '0003_assignmentscheduale_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentscheduale',
            name='assignment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='assignment.assignment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizscheduale',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.quizzes'),
            preserve_default=False,
        ),
    ]