# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0009_auto_20161029_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='greetings',
            new_name='cvlink',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='dateend',
            new_name='elaborate',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='oname',
            new_name='field',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='contact',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='sub1',
            new_name='work1',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='sub2',
            new_name='work2',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='sub3',
            new_name='work3',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='sub4',
            new_name='work4',
        ),
        migrations.RemoveField(
            model_name='event',
            name='datestart',
        ),
        migrations.RemoveField(
            model_name='event',
            name='fbid',
        ),
        migrations.RemoveField(
            model_name='event',
            name='logolink',
        ),
        migrations.RemoveField(
            model_name='event',
            name='tagline',
        ),
    ]
