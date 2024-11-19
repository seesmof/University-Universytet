from django.shortcuts import render
from django.http import HttpResponse

from .forms import NameForm

def home(request):
    if request.method=='POST':
        form=NameForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            return HttpResponse(username)
    if request.method=='GET':
        form = NameForm()
    return render(request, 'home.html', {'form':form})