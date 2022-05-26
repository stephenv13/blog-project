# Generated by Django 3.2.5 on 2022-05-04 02:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220503_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_dated',
        ),
        migrations.AddField(
            model_name='post',
            name='created_dated',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 2, 3, 31, 131947, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 2, 3, 31, 132918, tzinfo=utc)),
        ),
    ]