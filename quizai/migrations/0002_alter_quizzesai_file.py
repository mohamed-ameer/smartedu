# Generated by Django 3.2 on 2022-07-04 06:19

from django.db import migrations, models
import quizai.models


class Migration(migrations.Migration):

    dependencies = [
        ('quizai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizzesai',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=quizai.models.user_directory_path),
        ),
    ]