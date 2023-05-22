# views.py
from django.shortcuts import render
from .models import Wallet, Transfer

def transfer_view(request):
    if request.method == 'POST':
        sender_wallet = Wallet.objects.get(user=request.user)  # Assuming user is logged in and has a wallet
        receiver_wallet = Wallet.objects.get(user=request.POST['receiver'])  # Assuming receiver is specified in the form
        amount = request.POST['amount']  # Assuming amount is specified in the form

        # Perform validation on sender's balance and other conditions
        if sender_wallet.balance >= amount:
            # Deduct amount from sender's balance and save the updated balance
            sender_wallet.balance -= amount
            sender_wallet.save()

            # Add amount to the receiver's balance and save the updated balance
            receiver_wallet.balance += amount
            receiver_wallet.save()

            # Create a transfer record
            Transfer.objects.create(sender=sender_wallet, receiver=receiver_wallet, amount=amount)

            # Redirect or render a success message
            return render(request, 'success.html')
        else:
            # Render an error message for insufficient balance
            return render(request, 'error.html', {'message': 'Insufficient balance'})
    else:
        # Render the transfer form
        return render(request, 'transfer.html')
