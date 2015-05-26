# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='type',
            field=models.CharField(default=b'LI', max_length=2, choices=[(b'LI', b'Light bulb'), (b'TE', b'Temperature sensor')]),
            preserve_default=True,
        ),
    ]
