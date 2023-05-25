from django.urls import path
from .views import TransferAPIView

urlpatterns = [
    path('transactions/transfer', TransferAPIView.as_view(), name="Transfer API"),
] 