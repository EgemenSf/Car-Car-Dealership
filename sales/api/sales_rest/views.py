from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Salesperson, Customer, Sale, AutomobileVO
from .encoders import AutomobileVOEncoder, SaleEncoder, SalespersonEncoder, CustomerEncoder
import json


@require_http_methods(["GET", "POST"])
def salesperson_list(request):
    if request.method == 'GET':
        salespeople = Salesperson.objects.all()
        return JsonResponse(
            {'salespeople': salespeople},
            encoder=SalespersonEncoder,
            safe=False,
        )

    elif request.method == 'POST':
        data = json.loads(request.body)
        salesperson = Salesperson.objects.create(**data)
        return JsonResponse(
            salesperson,
            encoder=SalespersonEncoder,
            safe=False,
            status=200,
        )

@require_http_methods(["DELETE"])
def delete_salesperson(request, id):
    try:
        salesperson = Salesperson.objects.get(pk=id)
        salesperson.delete()
        return JsonResponse(
            {'status': 'success'},
            status=200
        )
    except Salesperson.DoesNotExist:
        return JsonResponse(
            {'error': 'Salesperson not found'},
            status=404
        )

@require_http_methods(["GET", "POST"])
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        return JsonResponse(
            {'customers': customers},
            encoder=CustomerEncoder,
            safe=False
        )
    elif request.method == 'POST':
        data = json.loads(request.body)
        customer = Customer.objects.create(**data)
        return JsonResponse(
            customer,
            encoder=CustomerEncoder,
            safe=False,
            status=200,
        )

@require_http_methods(["DELETE"])
def delete_customer(request, id):
    try:
        customer = Customer.objects.get(pk=id)
        customer.delete()
        return JsonResponse(
            {'status': 'success'},
            status=200
        )
    except Customer.DoesNotExist:
        return JsonResponse(
            {'error': 'Customer not found'},
            status=404
        )

@require_http_methods(["GET", "POST"])
def sale_list(request):
    if request.method == 'GET':
        sales = Sale.objects.all()
        return JsonResponse(
            {'sales': sales},
            encoder=SaleEncoder,
            safe=False,
        )
    elif request.method == 'POST':
        data = json.loads(request.body)

        try:
            automobile_vo = AutomobileVO.objects.get(vin=data.pop('automobileVin', None))
            salesperson = Salesperson.objects.get(pk=data.pop('salespersonId', None))
            customer = Customer.objects.get(pk=data.pop('customerId', None))


            sale = Sale.objects.create(
                automobile=automobile_vo,
                salesperson=salesperson,
                customer=customer,
                **data
            )

            return JsonResponse(
                sale,
                encoder=SaleEncoder,
                safe=False,
                status=200
            )
        except (AutomobileVO.DoesNotExist, Salesperson.DoesNotExist, Customer.DoesNotExist) as e:
            return JsonResponse(
                {'error': str(e)},
                status=404,
            )
        except KeyError as e:
            return JsonResponse(
                {'error': f'Missing field: {e}'},
                status=400
            )
        except Exception as e:
            return JsonResponse(
                {'error': str(e)},
                status=400,
            )

@require_http_methods(["DELETE"])
def delete_sale(request, id):
    try:
        sale = Sale.objects.get(pk=id)
        sale.delete()
        return JsonResponse(
            {'status': 'success'},
            status=200
        )
    except Sale.DoesNotExist:
        return JsonResponse(
            {'error': 'Sale not found'},
            status=404,
        )

@require_http_methods(["GET", "POST"])
def automobile_list(request):
    if request.method == 'GET':
        automobiles = AutomobileVO.objects.all()
        return JsonResponse(
            {'automobiles': automobiles},
            encoder=AutomobileVOEncoder,
            safe=False
        )
    elif request.method == 'POST':
        data = json.loads(request.body)
        automobile = AutomobileVO.objects.create(**data)
        return JsonResponse(
            automobile,
            encoder=AutomobileVOEncoder,
            safe=False,
            status=201
        )

@require_http_methods(["DELETE"])
def delete_automobile(request, id):
    try:
        automobile = AutomobileVO.objects.get(pk=id)
        automobile.delete()
        return JsonResponse(
            {'status': 'success'},
            status=204,
        )
    except AutomobileVO.DoesNotExist:
        return JsonResponse(
            {'error': 'Automobile not found'},
            status=404,
        )
