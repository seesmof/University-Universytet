from django.shortcuts import redirect, render
from .models import User, Transaction

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            return redirect('user_dashboard', user_id=user.id)
    return render(request, 'login.html')

def user_dashboard_view(request, user_id):
    user = User.objects.get(id=user_id)
    transactions = Transaction.objects.filter(user=user)
    return render(request, 'user_dashboard.html', {'user': user, 'transactions': transactions})

def add_transaction_view(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        date = request.POST.get('date')
        Transaction.objects.create(user=user, amount=amount, description=description, date=date)
        return redirect('user_dashboard', user_id=user.id)
    return render(request, 'add_transaction.html', {'user': user})

def delete_transaction_view(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    user_id = transaction.user.id
    transaction.delete()
    return redirect('user_dashboard', user_id=user_id)