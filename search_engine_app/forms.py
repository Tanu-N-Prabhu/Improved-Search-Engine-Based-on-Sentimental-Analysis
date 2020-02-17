from django import forms


class ContactForms(forms.Form):
    name=forms.CharField(label = '', widget=forms.TextInput(attrs={'placeholder':'  Search....'}))
