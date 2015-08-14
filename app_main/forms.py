__author__ = 'BUR'
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message

class FioForm(forms.Form):
    name        = forms.CharField(label='Имя', max_length=100)
    age         = forms.IntegerField(label='Возраст')
    mail        = forms.EmailField(required=False, label='Your e-mail address')
    desc        = forms.CharField(label='Примечание',widget=forms.Textarea)
    phone       = forms.CharField(label='Телефон', max_length=100)
    date_brd    = forms.DateField(label='Дата рождения')