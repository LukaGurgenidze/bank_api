from rest_framework import serializers, viewsets
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=("customer_id", "description", "balance")

