from django.core.management.base import BaseCommand
import os
from core import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        old_bar_codes = models.BarCode.objects.filter()
        os.remove("/home/mehdi/Documents/projects/IbstashInevntory/ibstsh_inventory/code_qr/96968db74111b46f09552d11f28e206e.png")