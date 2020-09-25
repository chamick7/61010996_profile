from django.shortcuts import render
from .forms import ContactForm


def home(req):
    if(req.method == 'POST'):
        print(req.POST)

    
    return render(req,'index.html',{'form':ContactForm})