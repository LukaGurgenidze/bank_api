from django.urls import path
from .views import add_account, retrieve_balance, retrieve_transaction_history


urlpatterns = [
    path('accounts/add', add_account, name="Add New Account to User"),
    path('accounts/<str:account_id>/balance', retrieve_balance, name="Balance"),
    path('accounts/<str:account_id>/transfer-history', retrieve_transaction_history, name="Transfer History"),
] 