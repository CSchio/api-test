from django.urls import path

from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('addReceipt/', views.CreateReceipt.as_view(), name='CreateReceipt'),
    path('addReceiptItem/', views.CreateReceiptItem.as_view(),
         name='CreateReceiptItem'),
]
