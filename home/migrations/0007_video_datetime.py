# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20150511_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 19, 38, 21, 45288, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
