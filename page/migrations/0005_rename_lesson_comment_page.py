# Generated by Django 3.2 on 2022-06-29 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='lesson',
            new_name='page',
        ),
    ]