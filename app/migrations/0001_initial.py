# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('roll_no', models.IntegerField(max_length=10)),
                ('branch', models.CharField(max_length=10)),
                ('session', models.IntegerField(max_length=4)),
                ('marks', models.IntegerField(max_length=4)),
                ('backlog', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
