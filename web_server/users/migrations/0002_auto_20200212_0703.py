# Generated by Django 2.2.9 on 2020-02-12 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.URLField(max_length=500, primary_key=True, serialize=False),
        ),
    ]
