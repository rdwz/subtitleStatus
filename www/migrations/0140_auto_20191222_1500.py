# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0139_subtitle_autotiming_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker_links',
            name='title',
            field=models.CharField(max_length=300, blank=True, default=''),
        ),
    ]
