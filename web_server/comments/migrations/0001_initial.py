# Generated by Django 2.2.5 on 2020-03-10 22:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('contentType', models.CharField(choices=[('text/plain', 'plain text'), ('text/markdown', 'markdown')], default='text/markdown', max_length=32)),
                ('content', models.TextField()),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
