# Generated by Django 3.2 on 2022-06-30 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_auto_20220629_1849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_given',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='user_given',
            new_name='user',
        ),
    ]