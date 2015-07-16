# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('many', '0002_auto_20150710_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='parents',
            field=models.ManyToManyField(to='many.Element', blank=True),
        ),
    ]
