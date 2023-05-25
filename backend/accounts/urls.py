from django.urls import path
from .views import AddAccountAPIView, retrieve_balance, retrieve_transaction_history


urlpatterns = [
    path('accounts/add', AddAccountAPIView.as_view(), name="Add New Account to User"),
    path('accounts/<str:account_id>/balance', retrieve_balance, name="Balance"),
    path('accounts/<str:account_id>/transfer-history', retrieve_transaction_history, name="Transfer History"),
] 