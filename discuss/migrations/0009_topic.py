# Generated by Django 3.0.8 on 2021-04-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0008_auto_20210404_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]