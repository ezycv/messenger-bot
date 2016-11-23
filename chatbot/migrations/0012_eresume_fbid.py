# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0011_auto_20161123_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='eresume',
            name='fbid',
            field=models.CharField(default=datetime.date(2016, 11, 23), max_length=250),
            preserve_default=False,
        ),
    ]
