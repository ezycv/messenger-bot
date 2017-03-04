# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0024_auto_20161204_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume_input',
            name='name',
            field=models.CharField(default=datetime.date(2016, 12, 4), max_length=250),
            preserve_default=False,
        ),
    ]
