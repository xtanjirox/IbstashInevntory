from django.contrib import admin
from . import models


admin.site.register(models.Size)
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Inventory)
admin.site.register(models.BarCode)
