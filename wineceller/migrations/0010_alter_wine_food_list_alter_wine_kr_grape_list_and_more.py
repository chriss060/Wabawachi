# Generated by Django 4.1.2 on 2022-11-16 09:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wineceller", "0009_remove_wine_created_at_remove_wine_updated_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wine",
            name="food_list",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=20), default=[], size=None
            ),
        ),
        migrations.AlterField(
            model_name="wine",
            name="kr_grape_list",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=20), default=[], size=None
            ),
        ),
        migrations.AlterField(
            model_name="wine",
            name="notes_list",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=20), default=[], size=None
            ),
        ),
    ]