# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0004_auto_20150603_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventDate',
            field=models.DateTimeField(),
        ),
    ]
