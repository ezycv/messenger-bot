# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0013_auto_20161128_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eresume',
            name='j',
            field=models.CharField(default=b'1', max_length=250),
        ),
    ]
