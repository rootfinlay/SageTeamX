from django import forms


class ContactForm(forms.Form):
    post = forms.CharField()
    