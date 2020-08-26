from apscheduler.schedulers.background import BackgroundScheduler
from django.db.models import Sum, FloatField,F
from receipt.models import Receipt, ReceiptItem
from django.utils import timezone
from .models import Stats

scheduler = BackgroundScheduler()

def updateStats():
    receipts = Receipt.objects.count()
    sells = ReceiptItem.objects.aggregate(price__sum=Sum(F('price') * F('quantity'),output_field=FloatField())).get('price__sum', 0.00)
    receiptsitems = ReceiptItem.objects.aggregate(Sum('quantity')).get('quantity__sum', 0.00)
    stat = Stats(receipts=receipts, sells=sells, receiptsitems=receiptsitems, created_at = timezone.now())
    stat.save(using='mongo')

def start_job():
    job = scheduler.add_job(updateStats, 'interval', seconds=7200)
    scheduler.start()
