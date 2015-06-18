# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0007_auto_20150605_0844'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='social',
            options={'ordering': ['-activitydate']},
        ),
    ]
