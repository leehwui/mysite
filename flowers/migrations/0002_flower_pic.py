# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='pic',
            field=models.ImageField(default=datetime.datetime(2015, 10, 4, 3, 7, 45, 75369, tzinfo=utc), upload_to='media/flowers_pics/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
