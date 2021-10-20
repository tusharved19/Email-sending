from django.shortcuts import render
# Create your views here.
from emailsend.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to codezilla'
        message = 'Hello'
        recepient = str(sub['Email'].value())
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = True)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})