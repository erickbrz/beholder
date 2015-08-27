# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_tips'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.TextField(max_length=255, unique=True, serialize=False, primary_key=True)),
                ('text', models.TextField(max_length=80)),
                ('dateOfCreation', models.DateTimeField()),
                ('author', models.ForeignKey(to='core.Person')),
                ('place', models.ForeignKey(to='core.Place')),
            ],
        ),
        migrations.RemoveField(
            model_name='tips',
            name='author',
        ),
        migrations.RemoveField(
            model_name='tips',
            name='place',
        ),
        migrations.DeleteModel(
            name='Tips',
        ),
    ]
