# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapy_coco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='challenge_data',
            field=models.TextField(blank=True),
        ),
    ]
