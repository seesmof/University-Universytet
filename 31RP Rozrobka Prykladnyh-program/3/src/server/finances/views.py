from django.shortcuts import render
from django.http import HttpResponse

def start(request):
    if request.method == 'POST':
        print(request.username)
    return render(request, 'start.html')

def user(request, user_name):
    print(user_name)
    return HttpResponse('ALLELUJAH')