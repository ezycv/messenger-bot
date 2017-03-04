# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_auto_20161019_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='state',
        ),
    ]
