from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.core import base_views as base
from apps.core import models, tables
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django_select2 import forms as s2forms
from apps.core import forms


# Create your views here.
def home(request):
    return render(request, 'index.html')


class SizeListView(base.BaseListView):
    model = models.Size
    table_class = tables.SizeTable
    table_pagination = False
    filter_class = None
    segment = 'Size'
    create_url = reverse_lazy('size-create')


class SizeCreateView(generic.CreateView, base.FormViewMixin):
    model = models.Size
    template_name = 'includes/create.html'
    fields = '__all__'
    segment = 'Size'

    def form_valid(self, form):
        sizes = form.cleaned_data['size_name'].split(',')
        for size in sizes:
            models.Size.objects.create(size_name=size.strip())
        return HttpResponseRedirect(models.Size.get_absolute_url(self))


class CategoryListView(base.BaseListView):
    model = models.Category
    table_class = tables.CategoryTable
    table_pagination = False
    filter_class = None
    segment = 'Category'
    create_url = reverse_lazy('category-create')


class CategoryCreateView(generic.CreateView, base.FormViewMixin):
    model = models.Category
    template_name = 'includes/create.html'
    form_class = forms.CategoryForm
    segment = 'Category'


class ProductListView(base.BaseListView):
    model = models.Product
    table_class = tables.ProductTable
    table_pagination = False
    filter_class = None
    segment = 'Product'
    create_url = reverse_lazy('product-create')


class ProductCreateView(generic.CreateView, base.FormViewMixin):
    model = models.Product
    template_name = 'includes/create.html'
    fields = '__all__'
    segment = 'Product'
    product = None


class InventoryListView(base.BaseListView):
    model = models.Inventory
    table_class = tables.InventoryTable
    table_pagination = False
    filter_class = None
    segment = 'Inventory'
    create_url = reverse_lazy('inventory-create')


class InventoryCreateView(generic.CreateView, base.FormViewMixin):
    model = models.Inventory
    template_name = 'includes/create.html'
    fields = ('product',)
    segment = 'Inventory'
    product = None

    def form_valid(self, form):
        product_id = form.cleaned_data['product']
        sizes = product_id.category.size.all()
        self.product = product_id
        for size in sizes:
            models.Inventory.objects.create(product=product_id, size=size)
        return HttpResponseRedirect(models.Inventory.get_absolute_url(self))


class InventoryDetailView(base.BaseListView):
    model = models.Inventory
    table_class = tables.InventoryDetailTable
    template_name = "includes/inventory_restock.html"
    table_pagination = False
    filter_class = None
    segment = 'Inventory'
    create_url = reverse_lazy('inventory-restock')

    def get_queryset(self):
        pk = self.kwargs['pk']
        print(super().get_queryset())
        return super().get_queryset().filter(product__id=pk)


class BarCodeListView(base.BaseListView):
    model = models.BarCode
    table_class = tables.BarCodeTable
    table_pagination = False
    filter_class = None
    segment = 'BarCode'
    create_url = reverse_lazy('inventory-create')

    def get_queryset(self):
        pk = self.kwargs['pk']
        return super().get_queryset().filter(inventory__id=pk)
