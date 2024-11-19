from django import forms

from .models import  PeriodicPayment

class NameForm(forms.Form):
    name = forms.CharField(label='Client name')

class DepositForm(forms.Form):
    amount = forms.IntegerField(label='Amount to deposit')
    purpose = forms.CharField()

class WithdrawForm(forms.Form):
    amount = forms.IntegerField(label='Amount to withdraw')
    purpose = forms.CharField()

class EditForm(forms.Form):
    name=forms.CharField()
    balance=forms.IntegerField()
    credit=forms.IntegerField()
    manager=forms.BooleanField(required=False)

class PeriodicForm(forms.Form):
    amount = forms.IntegerField(label='Amount to pay')
    period = forms.ChoiceField(choices=PeriodicPayment.PERIODS)
    purpose = forms.CharField()