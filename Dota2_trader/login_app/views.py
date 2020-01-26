from django.shortcuts import render
from Dota2_trader.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
from .models import User
# Create your views here.

def index(request):
    return render(request,'login_page.html')
    # return HttpResponse("hello")

def forget_password(request):
    return render(request,'forget_password/forget_password.html')

def password_reset_request(request):
    if request.method == 'POST':
        subject = 'password reset'
        message = 'localhost:8000/'
        recepient = str(sub['Email'].value())
        if not User.objects.filter(user_email=recepient).exists():
            return render(request, 'forget_password/failed.html', {'recepient': recepient})
        else:
            send_mail(subject,
                message, EMAIL_HOST_USER, [recepient], fail_silently=False)
            return render(request, 'forget_password/successed.html', {'form': sub})

def password_reset(request):
    if request.method == 'POST':
        account = User.objects.get(email=request.POST[email])
        return render(request, 'forget_password/reset_successed.html', {'form': sub})