# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hurtownia', '0008_auto_20150221_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photos2',
            field=models.ForeignKey(related_name='photos_of', to='hurtownia.Photo', null=True),
            preserve_default=True,
        ),
    ]
