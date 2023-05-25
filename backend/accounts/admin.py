from django.contrib import admin
from .models import Account

class AccountModelAdmin(admin.ModelAdmin):
    list_display=['account_id', 'created_at', 'balance']
    search_fields=['account_id', 'created_at', 'balance']
    list_per_page=10

admin.site.register(Account, AccountModelAdmin)
