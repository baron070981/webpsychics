from django import forms




class SendingNumberForm(forms.Form):
    number = forms.CharField(label='Введите задуманое число:', max_length=2)







