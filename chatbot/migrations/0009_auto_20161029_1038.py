# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0008_resume_input'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume_input',
            old_name='details_sub11',
            new_name='educational_qualifications_1',
        ),
        migrations.RenameField(
            model_name='resume_input',
            old_name='details_sub21',
            new_name='educational_qualifications_2',
        ),
        migrations.RemoveField(
            model_name='resume_input',
            name='details_sub22',
        ),
        migrations.RemoveField(
            model_name='resume_input',
            name='details_sub23',
        ),
        migrations.RemoveField(
            model_name='resume_input',
            name='details_sub24',
        ),
        migrations.RemoveField(
            model_name='resume_input',
            name='details_sub31',
        ),
        migrations.RemoveField(
            model_name='resume_input',
            name='details_sub32',
        ),
        migrations.RemoveField(
            model_name='resume_input',
            name='details_sub33',
        ),
        migrations.RemoveField(
            model_name='resume_input',
            name='details_sub34',
        ),
        migrations.RemoveField(
            model_name='resume_input',
            name='details_sub41',
        ),
        migrations.RemoveField(
            model_name='resume_input',
            name='details_sub42',
        ),
        migrations.RemoveField(
            model_name='resume_input',
            name='details_sub51',
        ),
        migrations.RemoveField(
            model_name='resume_input',
            name='details_sub52',
        ),
        migrations.RemoveField(
            model_name='resume_input',
            name='details_sub53',
        ),
        migrations.RemoveField(
            model_name='resume_input',
            name='details_sub54',
        ),
        migrations.AddField(
            model_name='resume_input',
            name='LinkedIn',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='city',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='dob',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='educational_qualifications_3',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='educational_qualifications_4',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='experience_1',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='experience_2',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='experience_3',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='experience_4',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='hobbies_1',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='hobbies_2',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='hobbies_3',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='hobbies_4',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='objective_achievements',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='objective_line1',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='skills_1',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='skills_2',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='skills_3',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume_input',
            name='skills_4',
            field=models.CharField(default=datetime.date(2016, 10, 29), max_length=100),
            preserve_default=False,
        ),
    ]
