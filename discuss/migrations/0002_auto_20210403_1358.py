# Generated by Django 3.0.8 on 2021-04-03 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussion',
            old_name='createion_time',
            new_name='creation_time',
        ),
    ]