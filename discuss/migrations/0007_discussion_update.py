# Generated by Django 3.0.8 on 2021-04-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0006_auto_20210403_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='update',
            field=models.BooleanField(default=False),
        ),
    ]
