from django.shortcuts import render

from .models import Account

def users_view(request):
    users = Account.objects.all()
    return render(request, 'users.html', {'users': users})

def user_view(request, user_id):
    user = Account.objects.filter(pk=user_id).first()
    return render(request, 'user.html', {'user': user})