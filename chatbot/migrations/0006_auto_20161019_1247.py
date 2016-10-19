# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0005_event_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='dates',
            new_name='dateend',
        ),
        migrations.AddField(
            model_name='event',
            name='datestart',
            field=models.CharField(default=datetime.date(2016, 10, 19), max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='oname',
            field=models.CharField(default=datetime.date(2016, 10, 19), max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=10000),
        ),
    ]
