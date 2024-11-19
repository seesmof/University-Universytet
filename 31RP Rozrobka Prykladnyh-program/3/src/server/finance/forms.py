from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Client name')

class DepositForm(forms.Form):
    amount = forms.IntegerField(label='Amount to deposit')

class WithdrawForm(forms.Form):
    amount = forms.IntegerField(label='Amount to withdraw')

class EditForm(forms.Form):
    name=forms.CharField()
    balance=forms.IntegerField()
    credit=forms.IntegerField()
    manager=forms.BooleanField(required=False)