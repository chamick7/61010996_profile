from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponse


def home(req):
    if(req.method == 'POST'):
        # print(req.POST)
        form = ContactForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']+' from '+from_email
            message = form.cleaned_data['message']

            try:
                send_mail(
                subject,
                message,
                from_email,
                ['sw.chal7.contact@gmail.com',from_email],
                fail_silently=False,
                )
            except Exception as e:
                print(e)


    
    return render(req,'index.html',{'form':ContactForm})