from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        print("YES LORD JESUS")
        print(request.user.username)
        logout(request)
    return HttpResponse('JESUS IS LORD')