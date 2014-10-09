# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20140923_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='author_blog',
            name='mail',
            field=models.EmailField(default='updateme@mail.kiss', max_length=75),
            preserve_default=False,
        ),
    ]
