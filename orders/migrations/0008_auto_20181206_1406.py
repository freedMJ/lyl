# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20181206_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'managed': True},
        ),
    ]
