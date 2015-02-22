# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hurtownia', '0007_auto_20150221_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='creator',
            field=models.ForeignKey(related_name='creator_of', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
