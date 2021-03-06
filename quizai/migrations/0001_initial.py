# Generated by Django 3.2 on 2022-07-11 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import quizai.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerAI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=900)),
                ('is_correct', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=900)),
                ('answers', models.ManyToManyField(to='quizai.AnswerAI')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuizzesAI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField(blank=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=quizai.models.user_directory_path)),
                ('points', models.PositiveIntegerField()),
                ('questions', models.ManyToManyField(to='quizai.QuestionAI')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AttempterAI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField()),
                ('completed', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizai.quizzesai')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AttemptAI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizai.answerai')),
                ('attempter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizai.attempterai')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizai.questionai')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizai.quizzesai')),
            ],
        ),
    ]
