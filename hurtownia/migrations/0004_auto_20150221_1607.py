# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hurtownia', '0003_auto_20150221_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='profile_image',
            new_name='image',
        ),
    ]
