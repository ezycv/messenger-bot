# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0004_remove_event_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='state',
            field=models.CharField(default=datetime.date(2016, 10, 19), max_length=1000),
            preserve_default=False,
        ),
    ]
