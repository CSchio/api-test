from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Receipt, ReceiptItem
import json


class CreateReceipt(View):
    def post(self, *args, **kwargs):
        receipt = Receipt()
        receipt.cpf = self.request.POST.get('cpf')
        receipt.cnpj = self.request.POST.get('cnpj')
        receipt.save()
        return HttpResponse()


class CreateReceiptItem(View):
    def post(self, *args, **kwargs):
        try: 
            receipt = Receipt.objects.get(id=self.request.POST.get('receipt_id'))
        except:
            return HttpResponse("Receipt not found",status=404)
        receiptItem = ReceiptItem()
        receiptItem.receipt_id = receipt
        receiptItem.name = self.request.POST.get('name')
        receiptItem.price = self.request.POST.get('price')
        receiptItem.quantity = self.request.POST.get('quantity')
        receiptItem.save()
        return HttpResponse()


class index(View):
    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        receipt = Receipt(
            cpf=data['cpf'], cnpj=data['cnpj'])
        receipt.save()
        for item in data['items']:
            ReceiptItem.objects.create(
                receipt_id=receipt, name=item['name'], price=item["price"], quantity=item["quantity"])
        return HttpResponse()

    def get(self, *args, **kwargs):
        return JsonResponse({"msg": "Hellow world"})
