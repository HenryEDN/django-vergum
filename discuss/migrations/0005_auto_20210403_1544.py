# Generated by Django 3.0.8 on 2021-04-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0004_auto_20210403_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='creation_time',
            field=models.DateField(auto_now=True),
        ),
    ]