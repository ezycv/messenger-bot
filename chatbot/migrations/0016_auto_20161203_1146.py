# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0015_auto_20161128_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eresume',
            name='cvlink',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='description',
            field=models.CharField(default=b'NULL', max_length=10000),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='elaborate',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='emailid',
            field=models.EmailField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='fbid',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='fblink',
            field=models.URLField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='field',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='location',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='mobile',
            field=models.IntegerField(default=b'NULL', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='name',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='state',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='twitterlink',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='work1',
            field=models.CharField(default=b'NULL', max_length=11250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='work2',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='work3',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='eresume',
            name='work4',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='LinkedIn',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='city',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='contact',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='dob',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='educational_qualifications_1',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='educational_qualifications_2',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='educational_qualifications_3',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='educational_qualifications_4',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='emailid',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='experience_1',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='experience_2',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='experience_3',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='experience_4',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='fbid',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='greetings',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='hobbies_1',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='hobbies_2',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='hobbies_3',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='hobbies_4',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='name',
            field=models.CharField(default=b'NULL', max_length=250),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='objective_achievements',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='objective_line1',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='skills_1',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='skills_2',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='skills_3',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='skills_4',
            field=models.CharField(default=b'NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume_input',
            name='state',
            field=models.CharField(default=b'NULL', max_length=1000),
        ),
    ]
