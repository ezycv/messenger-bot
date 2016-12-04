# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0017_auto_20161203_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eresume',
            name='field',
            field=models.CharField(default=b' ', max_length=250),
        ),
    ]
