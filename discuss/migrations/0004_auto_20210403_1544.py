# Generated by Django 3.0.8 on 2021-04-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0003_auto_20210403_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='creation_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
