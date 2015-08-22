# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapy_coco', '0005_auto_20150809_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenge',
            old_name='challenge_data',
            new_name='api_data',
        ),
        migrations.RenameField(
            model_name='challenge',
            old_name='is_challenge_data_json',
            new_name='is_api_data_json',
        ),
    ]
