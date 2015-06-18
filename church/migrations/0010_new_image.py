# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0009_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='image',
            field=models.ImageField(null=True, upload_to=b'news/%Y/%m/%d'),
        ),
    ]
