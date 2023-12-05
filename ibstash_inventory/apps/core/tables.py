import django_tables2 as tables
from apps.core import models


class SizeTable(tables.Table):
    class Meta:
        orderable = False
        model = models.Size
        fields = ('id', 'size_name',)
        attrs = {"class": "table", "id": "table2"}


class CategoryTable(tables.Table):
    class Meta:
        orderable = False
        model = models.Category
        fields = ('id', 'category_name', 'size')
        attrs = {"class": "table", "id": "table2"}


DETAIL_BUTTON_TEMPLATE = """
        <a href="{{record.get_absolute_url}}" class="btn btn-outline-primary"><i class='fas fa-pencil-alt'></i></a>
"""


class ProductTable(tables.Table):
    detail = tables.TemplateColumn(DETAIL_BUTTON_TEMPLATE)

    class Meta:
        orderable = False
        model = models.Product
        fields = ('id', 'product_name', 'category', 'detail')
        attrs = {"class": "table", "id": "table2"}


DETAIL_BUTTON_TEMPLATE_INVENTORY = """
        <a href="detail/{{record.product}}" class="btn btn-outline-primary"><i class='fas fa-pencil-alt'></i></a>
"""


class InventoryTable(tables.Table):
    detail = tables.TemplateColumn(DETAIL_BUTTON_TEMPLATE_INVENTORY)

    class Meta:
        orderable = False
        model = models.Inventory
        fields = ('product', 'product_name', 'stock_Quantity', 'detail')
        attrs = {"class": "table", "id": "table2"}


INPUT_BUTTON_TEMPLATE_INVENTORY = """
<div class="col-sm-2">
<input name="barcode_{{record.id}}" type="text" class="form-control" value="0"/>
</div>        
"""


class InventoryDetailTable(tables.Table):
    detail = tables.TemplateColumn(DETAIL_BUTTON_TEMPLATE)
    restock = tables.TemplateColumn(INPUT_BUTTON_TEMPLATE_INVENTORY)

    class Meta:
        orderable = False
        model = models.Inventory
        fields = ('id', 'product', 'size', 'quantity', 'restock', 'detail')
        attrs = {"class": "table", "id": "table2"}


FUNC_DETAIL_BUTTON_TEMPLATE = """
        <a href="/api/generate_code/{{record.inventory.id}}/{{record.id}}" class="btn icon btn-primary" title="Generated"><i class='fas fa-pencil-alt'></i></a>
        <a href="/api/stick_code/{{record.inventory.id}}/{{record.id}}" class="btn icon btn-warning" title="Sticked"><span class="fa-fw select-all fas"></span></a>
        <a href="/api/ship_code/{{record.inventory.id}}/{{record.id}}" class="btn icon btn-success" title="Shipped"><span class="fa-fw select-all fas"></span></a>
        <a href="/api/return_code/{{record.inventory.id}}/{{record.id}}" class="btn icon btn-danger" title="Return"><i class="bi bi-arrow-counterclockwise"></i></a>
"""


class BarCodeTable(tables.Table):
    detail = tables.TemplateColumn(FUNC_DETAIL_BUTTON_TEMPLATE)

    class Meta:
        orderable = False
        model = models.BarCode
        fields = ('inventory__product', 'inventory__size', 'barcode', 'barcode_status', 'detail')
        attrs = {"class": "table", "id": "table2"}
