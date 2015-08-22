# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapy_coco', '0006_auto_20150822_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='does_require_processing',
        ),
        migrations.AddField(
            model_name='challenge',
            name='handler',
            field=models.CharField(max_length=60, blank=True),
        ),
    ]
