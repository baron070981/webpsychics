from django import forms




class SendNumForm(forms.Form):
    number = forms.CharField(max_length=2,label='Введите задуманое ранее число')
    















