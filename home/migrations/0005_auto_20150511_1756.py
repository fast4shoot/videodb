# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20150511_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='state',
            field=models.CharField(default='U', max_length=1, choices=[('U', 'Zpracovává se'), ('P', 'Zpracováno'), ('E', 'Chyba zpracování')]),
        ),
    ]
