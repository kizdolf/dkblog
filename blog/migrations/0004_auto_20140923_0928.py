# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20140923_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author_blog',
            name='img',
            field=models.FileField(upload_to=b''),
        ),
    ]
