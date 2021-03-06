# Generated by Django 3.2 on 2022-07-11 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '__first__'),
        ('classroom', '0001_initial'),
        ('page', '__first__'),
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.DateTimeField(auto_now_add=True)),
                ('assignment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assignment.assignment')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.course')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='page.page')),
                ('quiz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.quizzes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
