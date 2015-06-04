# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapy_coco', '0003_auto_20150603_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='challenge_title',
            field=models.CharField(max_length=120, default='Challenge'),
            preserve_default=False,
        ),
    ]
