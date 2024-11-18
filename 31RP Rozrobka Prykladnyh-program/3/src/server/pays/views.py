from django.shortcuts import render

from .models import Account

def users_view(request):
    users = Account.objects.all()
    return render(request, 'users.html', {'users': users})