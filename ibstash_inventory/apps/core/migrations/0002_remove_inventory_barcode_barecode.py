# Generated by Django 4.2.6 on 2023-11-15 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inventory",
            name="barcode",
        ),
        migrations.CreateModel(
            name="BareCode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("barcode", models.CharField(default="HELLO CODE", max_length=20)),
                (
                    "inventory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.inventory",
                    ),
                ),
            ],
            options={
                "db_table": "barcode",
            },
        ),
    ]
