# Generated by Django 3.2.8 on 2021-10-22 21:52

import django.db.models.deletion
from django.db import migrations, models

import edd.fields


def bootstrap(apps, schema_editor):
    # create bootstrap objects
    Layout = apps.get_model("load", "Layout")
    LAYOUT_AMBR = Layout.objects.create(name="Ambr", description="")
    ParserMapping = apps.get_model("load", "ParserMapping")
    XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ParserMapping.objects.create(
        layout=LAYOUT_AMBR,
        mime_type=XLSX,
        parser_class="edd.load.parsers.AmbrExcelParser",
    )

    # create bootstrap objects -- MeasurementType
    bootstrap_measurement_type(apps)
    # create bootstrap objects -- MeasurementUnit
    boostrap_measurement_unit(apps)
    # create bootstrap objects -- DefaultUnit
    bootstrap_default_unit(apps)
    # create bootstrap objects -- MeasurementNameTransform
    bootstrap_measurement_name_transform(apps)


def bootstrap_measurement_type(apps):
    MeasurementType = apps.get_model("main", "MeasurementType")
    GENERIC = "_"
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="Volume of inocula",
        uuid="416b8a10-510c-40f7-85cb-5a5cae935644",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="Dry Cell Weight",
        uuid="350a597a-028b-42a0-9581-cf362f13a3ff",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC, type_name="pH", uuid="c60542ab-dcdb-4503-a2b5-55f5d8551728",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="Total Malonic Acid Formed",
        uuid="00a7e97f-53f5-44f8-a27f-8b6580673289",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="Temperature",
        uuid="97e7ba83-e15a-4dd1-aa11-d8411a67c2a4",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="Stir speed",
        uuid="57c5ec84-67e2-431b-a78e-85253373071e",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="Air flow",
        uuid="f8bb078e-bb43-44f9-8f1b-91a28726c274",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="Volume",
        uuid="d8e9f1ea-9991-44c3-ba8e-5ee25f44aba7",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="OUR",
        uuid="3a7482bf-c259-48db-8534-31a336681f5e",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="CER",
        uuid="b55b5d30-cfab-450c-ab2e-fdee4bfbd602",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="Volume",
        uuid="d8e9f1ea-9991-44c3-ba8e-5ee25f44aba7",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC, type_name="RQ", uuid="97ed0ed7-1eaa-4427-9c44-9712d5070e98",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="Feed volume pumped",
        uuid="bd88d980-c418-44be-b12d-4b1a6cda08d3",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="Base volume pumped",
        uuid="83c50be5-199f-4ef8-93fc-5db77b09e3c3",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="Acid volume pumped",
        uuid="15192dca-4863-475f-bf79-910bd722997a",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="Antifoam volume pumped",
        uuid="3a7ae3c2-c339-4c2c-821b-12d63dfcd39d",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="Volume sampled",
        uuid="0c88a7b1-ef9e-4271-9f54-e6e63869433c",
    )
    MeasurementType.objects.get_or_create(
        type_group=GENERIC,
        type_name="Dissolved Oxygen",
        uuid="b65fb9bc-4e63-4617-b143-bf08f8b44699",
    )


def boostrap_measurement_unit(apps):
    MeasurementUnit = apps.get_model("main", "MeasurementUnit")
    # constants on main.models.MeasurementType.Group
    GENERIC = "_"
    MeasurementUnit.objects.get_or_create(type_group=GENERIC, unit_name="lpm")
    MeasurementUnit.objects.get_or_create(type_group=GENERIC, unit_name="°C")
    MeasurementUnit.objects.get_or_create(type_group=GENERIC, unit_name="rpm")
    MeasurementUnit.objects.get_or_create(type_group=GENERIC, unit_name="°C")
    MeasurementUnit.objects.get_or_create(type_group=GENERIC, unit_name="mL")
    MeasurementUnit.objects.get_or_create(type_group=GENERIC, unit_name="mM/L/h")
    MeasurementUnit.objects.get_or_create(
        type_group=GENERIC, unit_name="% maximum measured"
    )


def bootstrap_default_unit(apps):
    MeasurementType = apps.get_model("main", "MeasurementType")
    MeasurementUnit = apps.get_model("main", "MeasurementUnit")
    DefaultUnit = apps.get_model("load", "DefaultUnit")

    GENERIC = "_"

    unit_obj = MeasurementUnit.objects.get(unit_name="°C")
    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC,
        type_name="Temperature",
        uuid="97e7ba83-e15a-4dd1-aa11-d8411a67c2a4",
    )
    DefaultUnit.objects.create(measurement_type=mes_obj, unit=unit_obj, parser="ambr")

    unit_obj = MeasurementUnit.objects.get(unit_name="rpm")
    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC,
        type_name="Stir speed",
        uuid="57c5ec84-67e2-431b-a78e-85253373071e",
    )
    DefaultUnit.objects.create(measurement_type=mes_obj, unit=unit_obj, parser="ambr")

    unit_obj = MeasurementUnit.objects.get(unit_name="n/a")
    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC, type_name="pH", uuid="c60542ab-dcdb-4503-a2b5-55f5d8551728",
    )
    DefaultUnit.objects.create(measurement_type=mes_obj, unit=unit_obj, parser="ambr")

    unit_obj = MeasurementUnit.objects.get(unit_name="lpm")
    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC,
        type_name="Air flow",
        uuid="f8bb078e-bb43-44f9-8f1b-91a28726c274",
    )
    DefaultUnit.objects.create(measurement_type=mes_obj, unit=unit_obj, parser="ambr")

    unit_obj = MeasurementUnit.objects.get(unit_name="% maximum measured")
    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC,
        type_name="Dissolved Oxygen",
        uuid="b65fb9bc-4e63-4617-b143-bf08f8b44699",
    )
    DefaultUnit.objects.create(measurement_type=mes_obj, unit=unit_obj, parser="ambr")

    unit_obj = MeasurementUnit.objects.get(unit_name="mM/L/h")
    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC,
        type_name="OUR",
        uuid="3a7482bf-c259-48db-8534-31a336681f5e",
    )
    DefaultUnit.objects.create(measurement_type=mes_obj, unit=unit_obj, parser="ambr")

    unit_obj = MeasurementUnit.objects.get(unit_name="mM/L/h")
    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC,
        type_name="CER",
        uuid="b55b5d30-cfab-450c-ab2e-fdee4bfbd602",
    )
    DefaultUnit.objects.create(measurement_type=mes_obj, unit=unit_obj, parser="ambr")

    unit_obj = MeasurementUnit.objects.get(unit_name="n/a")
    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC, type_name="RQ", uuid="97ed0ed7-1eaa-4427-9c44-9712d5070e98",
    )
    DefaultUnit.objects.create(measurement_type=mes_obj, unit=unit_obj, parser="ambr")

    unit_obj = MeasurementUnit.objects.get(unit_name="mL")
    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC,
        type_name="Feed volume pumped",
        uuid="bd88d980-c418-44be-b12d-4b1a6cda08d3",
    )
    DefaultUnit.objects.create(measurement_type=mes_obj, unit=unit_obj, parser="ambr")

    unit_obj = MeasurementUnit.objects.get(unit_name="mL")
    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC,
        type_name="Antifoam volume pumped",
        uuid="3a7ae3c2-c339-4c2c-821b-12d63dfcd39d",
    )
    DefaultUnit.objects.create(measurement_type=mes_obj, unit=unit_obj, parser="ambr")

    unit_obj = MeasurementUnit.objects.get(unit_name="mL")
    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC,
        type_name="Acid volume pumped",
        uuid="15192dca-4863-475f-bf79-910bd722997a",
    )
    DefaultUnit.objects.create(measurement_type=mes_obj, unit=unit_obj, parser="ambr")

    unit_obj = MeasurementUnit.objects.get(unit_name="mL")
    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC,
        type_name="Base volume pumped",
        uuid="83c50be5-199f-4ef8-93fc-5db77b09e3c3",
    )
    DefaultUnit.objects.create(measurement_type=mes_obj, unit=unit_obj, parser="ambr")

    unit_obj = MeasurementUnit.objects.get(unit_name="mL")
    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC,
        type_name="Volume sampled",
        uuid="0c88a7b1-ef9e-4271-9f54-e6e63869433c",
    )
    DefaultUnit.objects.create(measurement_type=mes_obj, unit=unit_obj, parser="ambr")

    unit_obj = MeasurementUnit.objects.get(unit_name="mL")
    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC,
        type_name="Volume of inocula",
        uuid="416b8a10-510c-40f7-85cb-5a5cae935644",
    )
    DefaultUnit.objects.create(measurement_type=mes_obj, unit=unit_obj, parser="ambr")


def bootstrap_measurement_name_transform(apps):
    MeasurementNameTransform = apps.get_model("load", "MeasurementNameTransform")
    MeasurementType = apps.get_model("main", "MeasurementType")

    GENERIC = "_"

    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC,
        type_name="Dissolved Oxygen",
        uuid="b65fb9bc-4e63-4617-b143-bf08f8b44699",
    )
    MeasurementNameTransform.objects.create(
        input_type_name="DO", edd_type_name=mes_obj, parser="ambr"
    )

    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC,
        type_name="Feed volume pumped",
        uuid="bd88d980-c418-44be-b12d-4b1a6cda08d3",
    )
    MeasurementNameTransform.objects.create(
        input_type_name="Feed#1 volume pumped", edd_type_name=mes_obj, parser="ambr"
    )

    mes_obj = MeasurementType.objects.get(
        type_group=GENERIC,
        type_name="Volume sampled",
        uuid="0c88a7b1-ef9e-4271-9f54-e6e63869433c",
    )
    MeasurementNameTransform.objects.create(
        input_type_name="Volume - sampled", edd_type_name=mes_obj, parser="ambr"
    )


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_edd_2_7"),
        ("load", "0002_builtin_bootstrap"),
    ]

    operations = [
        migrations.CreateModel(
            name="MeasurementNameTransform",
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
                (
                    "input_type_name",
                    edd.fields.VarCharField(
                        help_text="Name of this Measurement Type in input.",
                        verbose_name="Input Measurement Type",
                    ),
                ),
                ("parser", edd.fields.VarCharField(blank=True, null=True)),
                (
                    "edd_type_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.measurementtype",
                    ),
                ),
            ],
            options={"db_table": "measurement_name_transform",},
        ),
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
                        to="main.measurementtype",
                    ),
                ),
                (
                    "protocol",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.protocol",
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.measurementunit",
                    ),
                ),
            ],
            options={"db_table": "default_unit",},
        ),
        migrations.RunPython(code=bootstrap, reverse_code=migrations.RunPython.noop),
    ]
