# Generated by Django 3.2 on 2022-07-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0001_initial'),
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='modules',
            field=models.ManyToManyField(to='module.Module'),
        ),
    ]
