from django.db import models
import uuid
from transactions.models import Transaction

class Account(models.Model):
    """
    Represents an account.
    """
    customer_id =  models.CharField(default="", max_length=100)
    account_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    balance = models.FloatField(default=0)
    transaction_history = models.ManyToManyField(Transaction, blank=True)

    @property
    def transaction_history_array(self):
        """
        Retrieves the transaction history of the account, sorted by time in descending order.
        """
        return sorted(self.transaction_history.all(), key=lambda obj: obj.time, reverse=True)
