from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.core import models
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType


@receiver(post_save, sender=models.Product)
def log_mongo_transfer(sender, instance, created, **kwargs):
    if created:
        sizes = instance.category.size.all()
        for size in sizes:
            models.Inventory.objects.create(product=instance, size=size)