from ninja import Router
from ninja_extra import NinjaExtraAPI
from apps.core import models
from apps.api import utils

api = NinjaExtraAPI()
router = Router()


@router.post('/restock_inventory')
def restock_inventory(request):
    ids = [(int(element.split('_')[-1]), int(request.POST[element])) for element in request.POST if
           element.startswith('barcode_')]
    for id, new_stock in ids:
        element = models.Inventory.objects.get(pk=id)
        start_stock = element.quantity
        element.quantity = start_stock + new_stock
        element.save()
        for product_number in range(start_stock + 1, start_stock + new_stock + 1, 1):
            barcode = utils.generate_code(element.product.product_name, element.size.size_name, product_number)
            utils.generate_qr_code(barcode)
            pp = models.BarCode.objects.create(
                inventory=element,
                barcode=barcode,
                barcode_status=models.BarCodeStatus.GENERATED
            )
    return {}
