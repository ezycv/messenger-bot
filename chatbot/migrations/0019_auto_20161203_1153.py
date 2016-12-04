# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0018_auto_20161203_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eresume',
            name='state',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='state',
            field=models.CharField(max_length=1000),
        ),
    ]
