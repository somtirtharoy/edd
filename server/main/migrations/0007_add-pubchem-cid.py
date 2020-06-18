# Generated by Django 1.9.13 on 2017-07-06 01:54
# flake8: noqa

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("main", "0006_add-protein-strain-link")]

    operations = [
        migrations.AddField(
            model_name="metabolite",
            name="pubchem_cid",
            field=models.IntegerField(
                blank=True,
                help_text="Unique PubChem identifier",
                null=True,
                unique=True,
                verbose_name="PubChem CID",
            ),
        )
    ]
