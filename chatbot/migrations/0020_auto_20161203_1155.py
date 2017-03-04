# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0019_auto_20161203_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eresume',
            name='emailid',
            field=models.EmailField(max_length=1000),
        ),
    ]
