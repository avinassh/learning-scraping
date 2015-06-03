# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapy_coco', '0002_auto_20150603_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='does_require_processing',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='challenge',
            name='is_challenge_data_json',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
