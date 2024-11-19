from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import *
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
    client=Client.objects.get(pk=id)
    clients=None
    if client.manager:
        clients=Client.objects.all().values()
    return render(request, 'client.html', {'client':client,'clients':clients})

def deposit(request, id):
    client=Client.objects.get(pk=id)
    if request.method=='POST':
        form=DepositForm(request.POST)
        if form.is_valid():
            amount=form.cleaned_data['amount']
            if client.credit < amount:
                return redirect('client', id=client.id)
            client.balance+=amount
            client.credit-=amount
            client.save()
            return redirect('client', id=client.id)
    if request.method=='GET':
        form=DepositForm()
    return render(request, 'deposit.html', {'form':form,'client':client})

def withdraw(request, id):
    client=Client.objects.get(pk=id)
    if request.method=='POST':
        form=WithdrawForm(request.POST)
        if form.is_valid():
            amount=form.cleaned_data['amount']
            if client.balance < amount:
                return redirect('client', id=client.id)
            client.credit+=amount
            client.balance-=amount
            client.save()
            return redirect('client', id=client.id)
    if request.method=='GET':
        form=WithdrawForm()
    return render(request, 'withdraw.html', {'form':form,'client':client})

def edit(request, id, admin):
    client=Client.objects.get(pk=id)
    if request.method=='POST':
        form=EditForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            edited_client=Client.objects.filter(name=data['name']).first()
            return redirect('client', id=admin)
    if request.method=='GET':
        form=EditForm({'name':client.name,'balance':client.balance,'credit':client.balance,'manager':client.manager})
    return render(request, 'edit.html', {'form':form,'client':client})