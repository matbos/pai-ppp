# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hurtownia', '0005_photo_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='photos',
        ),
    ]
