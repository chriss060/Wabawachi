# Generated by Django 4.1.3 on 2022-11-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='wine',
        ),
        migrations.AddField(
            model_name='review',
            name='wine_id',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
