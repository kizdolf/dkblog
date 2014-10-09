# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_article_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='draft',
            field=models.BooleanField(default=b'true'),
        ),
    ]
