# Generated by Django 3.2 on 2022-07-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_attempter_course'),
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='quizzes',
            field=models.ManyToManyField(to='quiz.Quizzes'),
        ),
    ]
