from djongo import models
from receipt.models import Receipt, ReceiptItem

class Stats(models.Model):
    receipts = models.IntegerField(default=0)
    sells = models.FloatField(default=0)
    receiptsitems = models.IntegerField()
    created_at = models.DateTimeField(null=True)


