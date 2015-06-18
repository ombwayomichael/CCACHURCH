# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0002_auto_20150531_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialgallery',
            name='description',
        ),
        migrations.AlterField(
            model_name='event',
            name='eventImage',
            field=models.ImageField(null=True, upload_to=b'Events/images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resource',
            name='resourcefile',
            field=models.FileField(null=True, upload_to=b'Resources/files'),
            preserve_default=True,
        ),
    ]
