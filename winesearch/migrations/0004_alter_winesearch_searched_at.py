# Generated by Django 4.1.3 on 2022-11-21 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("winesearch", "0003_winesearch_searched_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="winesearch",
            name="searched_at",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]