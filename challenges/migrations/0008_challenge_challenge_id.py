# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0007_auto_20150822_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='challenge_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
