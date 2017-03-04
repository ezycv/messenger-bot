# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0007_auto_20161019_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume_input',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('greetings', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=1000)),
                ('fbid', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=250)),
                ('emailid', models.CharField(max_length=1000)),
                ('contact', models.CharField(max_length=100)),
                ('details_sub11', models.CharField(max_length=100)),
                ('details_sub21', models.CharField(max_length=100)),
                ('details_sub22', models.CharField(max_length=250)),
                ('details_sub23', models.CharField(max_length=250)),
                ('details_sub24', models.CharField(max_length=250)),
                ('details_sub31', models.CharField(max_length=250)),
                ('details_sub32', models.CharField(max_length=250)),
                ('details_sub33', models.CharField(max_length=250)),
                ('details_sub34', models.CharField(max_length=250)),
                ('details_sub41', models.CharField(max_length=250)),
                ('details_sub42', models.CharField(max_length=250)),
                ('details_sub51', models.CharField(max_length=250)),
                ('details_sub52', models.CharField(max_length=250)),
                ('details_sub53', models.CharField(max_length=250)),
                ('details_sub54', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
