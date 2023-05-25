from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Transaction
from accounts.models import Account

class TransferAPITestCase(APITestCase):
    def setUp(self):
        self.account1 = Account.objects.create(customer_id='test_customer_1', balance=100)
        self.account2 = Account.objects.create(customer_id='test_customer_2', balance=50)

    def test_successful_transfer(self):
        url = reverse('Transfer API')
        data = {
            'account_id': self.account1.account_id,
            'receiver_id': self.account2.account_id,
            'amount': 50
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Transaction.objects.count(), 1)
        self.account1.refresh_from_db()
        self.account2.refresh_from_db()
        self.assertEqual(self.account1.balance, 50)
        self.assertEqual(self.account2.balance, 100)

    def test_invalid_account_id(self):
        url = reverse('Transfer API')
        data = {
            'account_id': 'invalid_id',
            'receiver_id': self.account2.account_id,
            'amount': 50
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 'Invalid account_id')

    def test_insufficient_balance(self):
        url = reverse('Transfer API')
        data = {
            'account_id': self.account1.account_id,
            'receiver_id': self.account2.account_id,
            'amount': 200
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 'Not enough balance')


    def tearDown(self):
        self.account1.delete()
        self.account2.delete()
