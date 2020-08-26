from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Stats

class index(View):
    def get(self, *args, **kwargs):
        data = list(Stats.objects.using('mongo').all().values(
            'id','receipts', 'sells', 'receiptsitems', 'created_at'
            ).order_by('created_at'))
        categories = [str(s['created_at'].ctime()) for s in data]
        sells = [s['sells'] for s in data]
        receipts = [s['receipts'] for s in data]
        receiptsitems = [s['receiptsitems'] for s in data]
        context = {'categories': categories, 'sells': sells, 'receipts': receipts,
         'receiptsitems': receiptsitems}
        return render(self.request, 'summary/graph.html', context)
