# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('greetings', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('contact', models.IntegerField(max_length=100)),
                ('fbid', models.CharField(max_length=1000)),
                ('dates', models.CharField(max_length=1000)),
                ('fblink', models.URLField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('emailid', models.EmailField(max_length=1000)),
                ('logolink', models.URLField(max_length=1000)),
                ('state', models.IntegerField(max_length=1000)),
                ('location', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
    ]
