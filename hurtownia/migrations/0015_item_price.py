# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hurtownia', '0014_auto_20150222_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(default=1),
            preserve_default=True,
        ),
    ]
