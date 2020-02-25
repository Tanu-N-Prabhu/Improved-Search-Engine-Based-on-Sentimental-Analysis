from django import forms

# The below is the radio buttons options for the sentiments
sentimentOptions= [
    ('positve', 'Postive'),
    ('negative', 'Negative'),
    ('na', 'N/A'),
    
    ]

class GeneralForms(forms.Form):
    name = forms.CharField(label = '', widget=forms.TextInput(attrs={'placeholder':'  Search....'}))
    options = forms.CharField(label='Please select the sentiment', widget=forms.RadioSelect(choices=sentimentOptions))


class loginForm(forms.Form):
    uname = forms.CharField(label = 'Username', widget=forms.TextInput(attrs={'placeholder':' Username'}))
    pwd = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'placeholder':' Password'}))


class signUpForm(forms.Form):
    newName = forms.CharField(label = 'Enter you name', widget=forms.TextInput(attrs={'placeholder':' Enter your name'}))
    email = forms.CharField(label = 'Enter your e-mail address', widget = forms.TextInput(attrs = {'placeholder': ' Enter your E-mail address'}))
    pwd = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'placeholder':' Enter a new password'}))
    pwdr = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'placeholder':' Re-enter the password'}))
