from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import datetime

from .forms import *
from .models import Client, Payment, PeriodicPayment

def home(request):
    if request.method=='POST':
        form=NameForm(request.POST)
        if not form.is_valid():
            # error here
            return redirect('home')
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
    clients=Client.objects.all().values() if client.manager else None
    payments=Payment.objects.filter(client=client).values()
    periodic_payments=PeriodicPayment.objects.filter(client=client).values()
    return render(request, 'client.html', {'client':client,'clients':clients,'payments':payments,'periodic_payments':periodic_payments})

def deposit(request, id):
    client=Client.objects.get(pk=id)
    if request.method=='POST':
        form=DepositForm(request.POST)
        if not form.is_valid():
            return redirect('client', id=client.id)
        amount=form.cleaned_data['amount']
        if client.credit < amount:
            # error here
            return redirect('client', id=client.id)
        client.credit-=amount
        client.balance+=amount
        client.save()
        payment=Payment(client=client,timestamp=datetime.now(),purpose=form.cleaned_data['purpose'],amount=amount,operation=dict(Payment.OPERATIONS)['Deposit'],kind=dict(Payment.KINDS)['Single'])
        payment.save()
        return redirect('client', id=client.id)
    if request.method=='GET':
        form=DepositForm()
        return render(request, 'deposit.html', {'form':form,'client':client})

def withdraw(request, id):
    client=Client.objects.get(pk=id)
    if request.method=='POST':
        form=WithdrawForm(request.POST)
        if not form.is_valid():
            return redirect('client', id=client.id)
        amount=form.cleaned_data['amount']
        if client.balance < amount:
            # error here
            return redirect('client', id=client.id)
        client.balance-=amount
        client.credit+=amount
        client.save()
        payment=Payment(client=client,timestamp=datetime.now(),purpose=form.cleaned_data['purpose'],amount=amount,operation=dict(Payment.OPERATIONS)['Withdrawal'],kind=dict(Payment.KINDS)['Single'])
        payment.save()
        return redirect('client', id=client.id)
    if request.method=='GET':
        form=WithdrawForm()
        return render(request, 'withdraw.html', {'form':form,'client':client})

def edit(request, id, admin):
    client=Client.objects.get(pk=id)
    if request.method=='POST':
        form=EditForm(request.POST)
        if not form.is_valid():
            return redirect('client', id=client.id)
        data=form.cleaned_data
        edited_client=Client.objects.filter(name=data['name']).first()
        new_name=data['name']
        new_balance=data['balance']
        new_credit=data['credit']
        new_status=data['manager']
        edited_client.name=new_name
        edited_client.balance=new_balance
        edited_client.credit=new_credit
        edited_client.manager=new_status
        edited_client.save()
        return redirect('client', id=admin)
    if request.method=='GET':
        form=EditForm(initial=model_to_dict(client))
        return render(request, 'edit.html', {'form':form,'client':client,'admin':admin})
    
def periodic(request, id):
    client=Client.objects.get(pk=id)
    if request.method=='POST':
        form=PeriodicForm(request.POST)
        if not form.is_valid():
            return redirect('client',id=client.id)
        data=form.cleaned_data
        amount=data['amount']
        period=data['period']
        purpose=data['purpose']
        periodic_payment=PeriodicPayment(client=client,amount=amount,period=period,purpose=purpose)
        periodic_payment.save()
        return redirect('client',id=client.id)
    if request.method=='GET':
        form=PeriodicForm()
        return render(request, 'periodic.html', {'form':form,'client':client})