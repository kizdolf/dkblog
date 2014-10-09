# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20141001_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(),
        ),
    ]
