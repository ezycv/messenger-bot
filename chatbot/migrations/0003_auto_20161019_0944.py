# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_auto_20161019_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contact',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
