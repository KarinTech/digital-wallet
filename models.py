# models.py
from django.db import models

class Wallet(models.Model):
    # Define fields for wallet information (e.g., user, balance, etc.)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class Transfer(models.Model):
    # Define fields for transfer information (e.g., sender, receiver, amount, etc.)
    sender = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transfers_sent')
    receiver = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transfers_received')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)