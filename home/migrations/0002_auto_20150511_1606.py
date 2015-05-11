# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(related_name='comments', related_query_name='comment', to='home.Video', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='user',
            field=models.ForeignKey(related_name='videos', related_query_name='video', to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(related_name='comments', to=settings.AUTH_USER_MODEL, related_query_name='comment'),
        ),
    ]
