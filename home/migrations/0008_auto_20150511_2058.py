# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_video_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='id',
        ),
        migrations.AddField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 20, 58, 54, 565856, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=256, serialize=False, primary_key=True),
        ),
    ]
