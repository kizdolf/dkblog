# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author_blog',
            old_name='name',
            new_name='main_name',
        ),
        migrations.AddField(
            model_name='article',
            name='main_name',
            field=models.CharField(default='name to change', max_length=150),
            preserve_default=False,
        ),
    ]
