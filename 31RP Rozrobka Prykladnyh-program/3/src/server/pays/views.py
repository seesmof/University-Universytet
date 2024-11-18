from django.shortcuts import render

from .models import Account

def users_view(request):
    users = Account.objects.all().values()
    return render(request, 'users.html', {'users': users})