# Generated by Django 3.0.8 on 2021-04-15 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0014_auto_20210415_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='discussion_topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discuss.Topic'),
        ),
    ]
