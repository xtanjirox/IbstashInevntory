# Generated by Django 4.2.6 on 2023-12-08 23:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_barecode_barcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='barcode',
            name='generated_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 23, 9, 5, 214974)),
        ),
        migrations.AlterField(
            model_name='barcode',
            name='barcode_status',
            field=models.IntegerField(choices=[(0, 'Generated'), (1, 'Sticked'), (2, 'Shipped'), (3, 'Returned')]),
        ),
    ]
