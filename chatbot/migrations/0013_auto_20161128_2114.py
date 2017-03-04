# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0012_eresume_fbid'),
    ]

    operations = [
        migrations.AddField(
            model_name='eresume',
            name='i',
            field=models.CharField(default=b'0', max_length=250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eresume',
            name='j',
            field=models.CharField(default=b'0', max_length=250),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eresume',
            name='work1',
            field=models.CharField(max_length=11250),
        ),
    ]
