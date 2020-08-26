from django.contrib import admin
from . import models

class ReceiptItemInline(admin.TabularInline):
    model = models.ReceiptItem
    extra = 0

class ReceiptAdmin(admin.ModelAdmin):
    inlines = [ReceiptItemInline]

admin.site.register(models.Receipt, ReceiptAdmin)
admin.site.register(models.ReceiptItem)
