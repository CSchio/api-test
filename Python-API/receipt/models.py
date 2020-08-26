from django.db import models


class Receipt(models.Model):
    cpf = models.CharField(max_length=14)
    cnpj = models.CharField(max_length=18)


class ReceiptItem(models.Model):
    receipt_id = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Product")
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
            return self.name
