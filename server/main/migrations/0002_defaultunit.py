# Generated by Django 2.2.23 on 2021-09-22 14:41

import django.db.models.deletion
from django.db import migrations, models

import edd.fields


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_edd_2_7"),
    ]

    operations = [
        migrations.CreateModel(
            name="DefaultUnit",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("parser", edd.fields.VarCharField(blank=True, null=True)),
                (
                    "measurement_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.MeasurementType",
                    ),
                ),
                (
                    "protocol",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.Protocol",
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.MeasurementUnit",
                    ),
                ),
            ],
            options={"db_table": "default_unit",},
        ),
    ]
