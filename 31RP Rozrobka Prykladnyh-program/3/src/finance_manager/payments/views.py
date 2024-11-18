from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Account, Transaction

# Create your views here.
@login_required
def account_overview(request):
    account = get_object_or_404(Account, user=request.user)
    transactions = Transaction.objects.filter(account=account)
    return render(request, 'account_overview.html', {'account': account, 'transactions': transactions})