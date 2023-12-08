from django.db import models
from django.urls import reverse_lazy
from datetime import datetime

class BarCodeStatus(models.IntegerChoices):
    GENERATED = 0, 'Generated'
    STICKED = 1, 'Sticked'
    SHIPPED = 2, 'Shipped'
    RETURNED = 3, 'Returned'


class Size(models.Model):
    size_name = models.CharField(max_length=150)

    class Meta:
        db_table = 'size'

    def __str__(self):
        return self.size_name

    def get_absolute_url(self):
        return reverse_lazy('size-list')


class Category(models.Model):
    category_name = models.CharField(max_length=20)
    size = models.ManyToManyField(Size)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse_lazy('category-list')


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse_lazy('product-list')


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'inventory'

    def __str__(self):
        return str(self.product) + ' - ' + str(self.size)

    def get_absolute_url(self):
        return reverse_lazy('barcode-detail', kwargs={"pk": self.pk})

    def get_product_absolute_url(self):
        return reverse_lazy('inventory-detail', kwargs={"pk": self.product.id})


class BarCode(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.DO_NOTHING)
    barcode = models.CharField(max_length=20, default='HELLO CODE')
    barcode_status = models.IntegerField(choices=BarCodeStatus.choices)
    generated_date = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'barcode'

