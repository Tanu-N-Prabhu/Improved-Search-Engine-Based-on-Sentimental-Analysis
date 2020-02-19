from django import forms

# The below is the radio buttons options for the sentiments
sentimentOptions= [
    ('positve', 'Postive'),
    ('negative', 'Negative'),
    ('na', 'N/A'),
    
    ]

class ContactForms(forms.Form):
    name = forms.CharField(label = '', widget=forms.TextInput(attrs={'placeholder':'  Search....'}))


class radioButtons(forms.Form):
    options = forms.CharField(label='Please select the sentiment', widget=forms.RadioSelect(choices=sentimentOptions))
