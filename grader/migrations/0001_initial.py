# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f', models.FileField(upload_to=b'')),
                ('name', models.CharField(default=b'', max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
