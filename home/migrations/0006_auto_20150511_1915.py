# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20150511_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='file',
        ),
        migrations.RemoveField(
            model_name='video',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='video',
            name='duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='state',
            field=models.CharField(choices=[('0', 'Zpracovává se'), ('R', 'Zpracovává se'), ('P', 'Zpracováno'), ('E', 'Chyba zpracování')], max_length=1, default='0'),
        ),
    ]
