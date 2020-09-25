from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='',required=True,widget=forms.TextInput(attrs={'class': 'contact_input input_name','placeholder':'Name'}))
    email = forms.EmailField(label='',required=True,widget=forms.TextInput(attrs={'class': 'contact_input input_email','placeholder':'Email'}))
    subject = forms.CharField(label='',required=True,widget=forms.TextInput(attrs={'class': 'contact_input input_subject','placeholder':'Subject'}))
    message = forms.CharField(label='',required=True,widget=forms.Textarea(attrs={'class': 'contact_input input_message','placeholder':'Message'}))