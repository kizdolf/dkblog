# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20140923_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author_blog',
            name='img',
            field=models.ImageField(upload_to=b'img/authors'),
        ),
    ]
