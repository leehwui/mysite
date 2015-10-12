# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0002_flower_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='pic',
            field=models.ImageField(upload_to='media/flower_pics/%Y/%m/%d'),
        ),
    ]
