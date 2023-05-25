from django.contrib import admin
from .models import Transaction

class TransactionModelAdmin(admin.ModelAdmin):
    list_display=['account_id', 'receiver_id', 'time', 'amount', 'transaction_id']
    search_fields=['account_id', 'receiver_id', 'time', 'amount', 'transaction_id']
    list_per_page=10

admin.site.register(Transaction, TransactionModelAdmin)