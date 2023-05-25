from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from .serializers import AccountSerializer
from .models import Account
from transactions.serializers import TransactionSerializer


@api_view(['POST'])
def add_account(request):
    """
    Retrieve account details.

    This function retrieves the details of all accounts and returns them as a response.

    Parameters:
    - request: The request object.

    Returns:
    - Response: The serialized account details.
    """
    try:
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        new_account = Account.objects.create(
            customer_id=validated_data["customer_id"],
            balance=validated_data["balance"],
            description=validated_data["description"]
        )

        return Response({"account_id": new_account.account_id})

    except Exception as e:
        return Response({"status": 500, "error": str(e)})


@api_view(['GET'])
def retrieve_transaction_history(request, account_id):
    """
    Retrieve transaction history.

    This function retrieves the transaction history for a specific account and returns it as a response.

    Parameters:
    - request: The request object.
    - account_id: The ID of the account.

    Returns:
    - Response: The serialized transaction history.
    """
    try:
        account = get_object_or_404(Account, account_id=account_id)
        transfer_history = account.transaction_history_array
        expense_history = []
        income_history = []
        all_transactions = []

        for transaction in transfer_history:
            serialized_transaction = TransactionSerializer(transaction).data
            all_transactions.append(serialized_transaction)

            if transaction.receiver_id == account.account_id:
                income_history.append(serialized_transaction)
            else:
                expense_history.append(serialized_transaction)

        return Response({
            'all': all_transactions,
            'income': income_history,
            'expense': expense_history
        })

    except Exception as e:
        return Response({"status": 500, "error": str(e)})


@api_view(['GET'])
def retrieve_balance(request, account_id):
    """
    Retrieve account balance.

    This function retrieves the balance for a specific account and returns it as a response.

    Parameters:
    - request: The request object.
    - account_id: The ID of the account.

    Returns:
    - Response: The account balance.
    """
    try:
        account = get_object_or_404(Account, account_id=account_id)
        balance = account.balance

        return Response({'balance': balance})

    except Exception as e:
        return Response({"status": 500, "error": str(e)})
