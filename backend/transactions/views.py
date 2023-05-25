from django.shortcuts import render
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework import generics, status
from rest_framework.generics import RetrieveUpdateAPIView
from accounts.models import Account
import uuid
from django.db import transaction


class TransferAPIView(generics.GenericAPIView):
    serializer_class = TransactionSerializer

    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        """
        Transfer funds between accounts.

        This function allows transferring funds from one account to another.

        Parameters:
        - request: The request object.
        - args: Additional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - Response: The serialized transaction details.
        """
        try:
            data = request.data
            account_id = data.get("account_id")
            receiver_id = data.get("receiver_id")
            amount = float(data.get("amount"))

            if is_not_valid_uuid(account_id):
                return Response("Invalid account_id")

            if is_not_valid_uuid(receiver_id):
                return Response("Invalid receiver_id")

            account = Account.objects.filter(account_id=account_id).first()
            receiver_account = Account.objects.filter(account_id=receiver_id).first()

            if not account:
                return Response("Account not found")

            if not receiver_account:
                return Response("Receiver account not found")

            if account.balance - amount < 0:
                return Response("Not enough balance")

            with transaction.atomic():
                # Create a new transaction
                new_transaction = Transaction.objects.create(account_id=data["account_id"], receiver_id=data["receiver_id"], amount=amount)

                # Update account balances
                account.balance -= amount
                receiver_account.balance += amount

                # Add transaction to account's transaction history
                account.transaction_history.add(new_transaction)
                receiver_account.transaction_history.add(new_transaction)

                # Save changes to the database
                account.save()
                receiver_account.save()

            return Response(TransactionSerializer(new_transaction).data)

        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def is_not_valid_uuid(value):
    try:
        uuid.UUID(str(value))
        return False
    except ValueError:
        return True
