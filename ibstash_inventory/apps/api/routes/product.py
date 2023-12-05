from ninja import Router
from ninja_extra import NinjaExtraAPI
from apps.core import models
from apps.api import utils
from django.shortcuts import render, redirect

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


@router.get('/generate_code/{inventory_id}/{item_id}')
def generate_code(request, inventory_id: int, item_id: int):
    item = models.BarCode.objects.get(pk=item_id)
    item.barcode_status = models.BarCodeStatus.GENERATED
    item.save()
    return redirect(f'/barcode/detail/{inventory_id}')


@router.get('/stick_code/{inventory_id}/{item_id}')
def stick_code(request,  inventory_id: int, item_id: int):
    item = models.BarCode.objects.get(pk=item_id)
    item.barcode_status = models.BarCodeStatus.STICKED
    item.save()
    return redirect(f'/barcode/detail/{inventory_id}')


@router.get('/ship_code/{inventory_id}/{item_id}')
def ship_code(request, inventory_id: int, item_id: int):
    item = models.BarCode.objects.get(pk=item_id)
    item.barcode_status = models.BarCodeStatus.SHIPPED
    item.save()
    return redirect(f'/barcode/detail/{inventory_id}')


@router.get('/return_code/{inventory_id}/{item_id}')
def return_code(request, inventory_id: int, item_id: int):
    item = models.BarCode.objects.get(pk=item_id)
    item.barcode_status = models.BarCodeStatus.RETURNED
    item.save()
    return redirect(f'/barcode/detail/{inventory_id}')
