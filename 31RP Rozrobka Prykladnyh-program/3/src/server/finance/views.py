from django.shortcuts import render
from django.http import HttpResponse

from .forms import NameForm

def home(request):
    if request.method=='POST':
        form=NameForm(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['user_name']
            return HttpResponse(user_name)
    if request.method=='GET':
        form = NameForm()
    return render(request, 'home.html', {'form':form})