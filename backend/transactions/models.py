from django.db import models
import uuid 

class Transaction(models.Model):
    account_id = models.CharField(default = "", max_length=100)
    receiver_id = models.CharField(default = "", max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(default=0)
    transaction_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)

    class Meta:
        ordering = ['-time']