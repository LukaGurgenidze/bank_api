from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import Account

class AccountTests(APITestCase):
    def test_add_account(self):
        url = reverse('Add New Account to User')
        data = {
            'customer_id': 'new_test_customer',
            'description': 'Checking',
            'balance': 1000
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('account_id', response.data)

        account_id = response.data['account_id']

    def test_retrieve_balance(self):
        new_account = Account.objects.create(customer_id = "new_customer", description="new account", balance = 100)
        url = reverse('Balance', args=[new_account.account_id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('balance', response.data)

    def test_retrieve_transaction_history(self):
        new_account = Account.objects.create(customer_id = "new_customer", description="new account", balance = 100)
        url = reverse('Transfer History', args=[new_account.account_id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('all', response.data)
        self.assertIn('income', response.data)
        self.assertIn('expense', response.data)
