# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20140929_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(to='blog.Article'),
            preserve_default=True,
        ),
    ]
