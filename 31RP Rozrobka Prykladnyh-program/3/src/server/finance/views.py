from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import NameForm,DepositForm
from .models import Client

def home(request):
    if request.method=='POST':
        form=NameForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            client=Client.objects.filter(name=name).first()
            if not client:
                client=Client(name=name)
                client.save()
            return redirect('client', id=client.id)
    if request.method=='GET':
        form = NameForm()
    return render(request, 'home.html', {'form':form})

def client(request, id):
    client=Client.objects.filter(pk=id).first()
    return render(request, 'client.html', {'client':client})

def deposit(request, id):
    client=Client.objects.filter(pk=id).first()
    if request.method=='POST':
        form=DepositForm(request.POST)
        if form.is_valid():
            amount=form.cleaned_data['amount']
            if amount>client.credit:
                # process error here
                pass
            client.balance+=amount
            client.credit-=amount
            return redirect(client, 'client.html', {'client':client})
    if request.method=='GET':
        form=DepositForm()
    return render(request, 'deposit.html', {'form':form,'client':client})