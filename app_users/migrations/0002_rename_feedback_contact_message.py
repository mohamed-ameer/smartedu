# Generated by Django 3.2 on 2022-07-09 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='feedback',
            new_name='message',
        ),
    ]