# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_quote_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='draft',
            field=models.BooleanField(default='false'),
            preserve_default=False,
        ),
    ]
