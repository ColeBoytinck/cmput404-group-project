# Generated by Django 3.0.2 on 2020-02-01 04:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('source', models.URLField()),
                ('origin', models.URLField()),
                ('description', models.CharField(max_length=512)),
                ('contentType', models.CharField(choices=[('Text', (('text/plain', 'plain text'), ('text/markdown', 'markdown'))), ('Image', (('image/png;base64', 'png'), ('image/jpeg;base64', 'jpeg'))), ('application/base64', 'base64 encoded')], default='text/markdown', max_length=32)),
                ('content', models.TextField()),
                ('count', models.PositiveIntegerField()),
                ('size', models.PositiveIntegerField()),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('visibility', models.CharField(choices=[('PUBLIC', 'Public'), ('FOAF', 'FOAF'), ('FRIENDS', 'Friends'), ('PRIVATE', 'Private'), ('SERVERONLY', 'Server Admins Only')], default='FRIENDS', max_length=16)),
                ('unlisted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authors.Author')),
            ],
        ),
    ]
