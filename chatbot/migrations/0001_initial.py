# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('greetings', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('contact', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=1000)),
                ('fbid', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
