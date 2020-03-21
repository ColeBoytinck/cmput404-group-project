# Generated by Django 2.1.5 on 2020-03-21 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='id',
        ),
        migrations.AlterField(
            model_name='node',
            name='foreign_server_hostname',
            field=models.URLField(max_length=500, primary_key=True, serialize=False, unique=True),
        ),
    ]
