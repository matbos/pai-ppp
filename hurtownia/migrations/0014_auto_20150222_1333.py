# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hurtownia', '0013_auto_20150222_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='superCategory',
            field=models.ForeignKey(default=None, blank=True, to='hurtownia.Category', null=True),
            preserve_default=True,
        ),
    ]
