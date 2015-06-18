# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('eventImage', models.ImageField(upload_to=b'')),
                ('venue', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('eventDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=40)),
                ('picture', models.ImageField(null=True, upload_to=b'Leaders/profile')),
                ('message', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
                ('patron', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MinistryCalender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.CharField(max_length=100)),
                ('eventDescription', models.CharField(max_length=100)),
                ('event_date', models.DateTimeField()),
                ('venue', models.CharField(max_length=100)),
                ('ministry', models.ForeignKey(to='church.Ministry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
                ('resourceimage', models.ImageField(null=True, upload_to=b'Resources/images')),
                ('resourcefile', models.FileField(null=True, upload_to=b'Resource/files')),
                ('views', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=128)),
                ('publish', models.BooleanField(default=False)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('details', models.TextField()),
                ('dateposted', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-dateposted'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SermonComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=42)),
                ('email', models.EmailField(max_length=75)),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('sermon', models.ForeignKey(to='church.Sermon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('servicedate', models.DateTimeField()),
                ('service', models.CharField(max_length=100, choices=[(b'Sunday school service', b'Sunday school service'), (b'Youth Service', b'Youth Service'), (b'First Service', b'First Service'), (b'Second Service', b'Second Service'), (b'Third Service', b'Third Service')])),
                ('preacher', models.CharField(max_length=100)),
                ('programmer', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-servicedate'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity', models.CharField(max_length=100)),
                ('activitydate', models.DateTimeField()),
                ('activitydescription', models.TextField()),
                ('slug', models.SlugField()),
                ('siteimage', models.ImageField(null=True, upload_to=b'socialsiteimages/%Y/%m/%d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialGallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b"activities/images/%Y/%m/%d'")),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('title', models.ForeignKey(to='church.Social')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
