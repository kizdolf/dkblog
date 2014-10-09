# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20140923_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(max_length=15000),
        ),
    ]
