from django.shortcuts import render

from .models import *

def users_view(request):
    users = Account.objects.all()
    return render(request, 'users.html', {'users': users})

def user_view(request, user_id):
    user = Account.objects.filter(pk=user_id).first()
    payments = Pay.objects.filter(user=user.id)
    users=None
    if user.manager:
        users = Account.objects.all().values()
    context={
        'user':user,
        'payments':payments,
        'users':users
    }
    return render(request, 'user.html', context)