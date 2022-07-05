# Generated by Django 3.2 on 2022-07-05 13:43

import app_users.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0013_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('feedback', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('picture', models.ImageField(blank=True, null=True, upload_to=app_users.models.user_directory_path_profile, verbose_name='Picture')),
                ('phone', models.CharField(max_length=15)),
                ('college_id', models.CharField(max_length=20)),
                ('univeristy_name', models.CharField(choices=[('Zagazig_University', 'Zagazig _University'), ('Cairo_University', 'Cairo_University'), ('Ain_Shams_University', 'Ain_Shams_University')], default='Zagazig_University', max_length=30)),
                ('major_types', models.CharField(choices=[('civil_engineering', 'civil_engineering'), ('chemical_engineering', 'chemical_engineering'), ('mechanical_engineering', 'mechanical_engineering'), ('electrical_engineering', 'electrical_engineering'), ('industrial_engineering', 'industrial_engineering')], default='electrical_engineering', max_length=30)),
                ('facebook', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('user_type', models.CharField(choices=[('student', 'student'), ('teacher', 'teacher')], default='student', max_length=10)),
                ('points', models.PositiveIntegerField(default=0, verbose_name='points')),
            ],
        ),
    ]
