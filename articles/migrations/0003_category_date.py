# Generated by Django 3.0.5 on 2020-04-24 15:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 4, 24, 15, 12, 53, 481189, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
