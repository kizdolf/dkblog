# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20140923_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(max_length=300),
        ),
    ]
