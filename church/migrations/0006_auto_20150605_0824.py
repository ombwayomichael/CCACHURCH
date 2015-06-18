# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0005_auto_20150605_0820'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['eventDate']},
        ),
    ]
