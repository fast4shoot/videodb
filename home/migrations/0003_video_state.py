# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150511_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='state',
            field=models.CharField(default='U', choices=[('U', 'Zpracovává se'), ('P', 'Zpracováno')], max_length=1),
        ),
    ]
