from mypage.models import Contact
from django import forms
from django.core import validators
class ContactForm(forms.ModelForm):
    class  meta():
        model = Contact
        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'textinputclass','placeholder': 'Name','text-align' :'center' ,'color':'black'}),
            'Name': forms.TextInput(attrs={'class': 'textinputclass','placeholder': 'Email','text-align' :'center' ,'color':'black'}),
            'message': forms.Textarea(attrs={'placeholder': 'message','color':'black'}),
        }
