# Generated by Django 3.0.8 on 2021-04-04 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0007_discussion_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussion',
            old_name='update',
            new_name='updated',
        ),
    ]