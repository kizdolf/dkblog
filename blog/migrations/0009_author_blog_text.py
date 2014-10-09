# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_link_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='author_blog',
            name='text',
            field=models.TextField(default="wel, here please put some words about you. Yeah it's a new feature!"),
            preserve_default=False,
        ),
    ]
