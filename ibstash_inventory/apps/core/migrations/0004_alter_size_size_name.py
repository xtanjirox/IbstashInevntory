# Generated by Django 4.2.6 on 2023-11-18 15:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_barecode_barcode_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="size",
            name="size_name",
            field=models.CharField(max_length=150),
        ),
    ]
