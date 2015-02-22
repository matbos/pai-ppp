# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hurtownia', '0004_auto_20150221_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='item',
            field=models.ForeignKey(blank=True, to='hurtownia.Item', null=True),
            preserve_default=True,
        ),
    ]
