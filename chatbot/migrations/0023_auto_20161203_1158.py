# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0022_auto_20161203_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eresume',
            name='mobile',
            field=models.CharField(max_length=100),
        ),
    ]
