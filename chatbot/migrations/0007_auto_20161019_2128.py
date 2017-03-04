# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0006_auto_20161019_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='sub1',
            field=models.CharField(default=datetime.date(2016, 10, 19), max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='sub2',
            field=models.CharField(default=datetime.date(2016, 10, 19), max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='sub3',
            field=models.CharField(default=datetime.date(2016, 10, 19), max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='sub4',
            field=models.CharField(default=datetime.date(2016, 10, 19), max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='tagline',
            field=models.CharField(default=datetime.date(2016, 10, 19), max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='twitterlink',
            field=models.CharField(default=datetime.date(2016, 10, 19), max_length=250),
            preserve_default=False,
        ),
    ]
