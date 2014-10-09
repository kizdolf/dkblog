# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='author',
            field=models.CharField(default='unknown', max_length=40),
            preserve_default=False,
        ),
    ]
