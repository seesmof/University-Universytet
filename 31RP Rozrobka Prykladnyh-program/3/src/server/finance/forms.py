from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Client name')

class DepositForm(forms.Form):
    amount = forms.IntegerField(label='Amount to deposit')

class WithdrawForm(forms.Form):
    amount = forms.IntegerField(label='Amount to withdraw')
