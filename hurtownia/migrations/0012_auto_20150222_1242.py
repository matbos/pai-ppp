# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hurtownia', '0011_auto_20150222_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='visible',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 2, 22, 11, 42, 45, 691000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
