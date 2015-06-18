# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leader',
            name='user',
        ),
        migrations.AddField(
            model_name='leader',
            name='cell',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='leader',
            name='email',
            field=models.EmailField(max_length=75, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='leader',
            name='firstname',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='leader',
            name='lastname',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='leader',
            name='website',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sermon',
            name='author',
            field=models.CharField(max_length=300),
            preserve_default=True,
        ),
    ]
