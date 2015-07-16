# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('many', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='elements_connected',
        ),
        migrations.AddField(
            model_name='element',
            name='parents',
            field=models.ManyToManyField(related_name='parents_rel_+', to='many.Element', blank=True),
        ),
    ]
