# Generated by Django 1.9.11 on 2017-04-12 23:38
# flake8: noqa

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("branding", "0002_auto_20170309_1713")]

    operations = [
        migrations.AlterField(
            model_name="branding",
            name="favicon_file",
            field=models.ImageField(null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="branding",
            name="logo_file",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
