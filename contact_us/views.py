from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def send_email(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone= request.POST['phone']
        
        send_mail(
            "Hello I Want To Connect With Your Company:",
            f"{name}\n{phone},\n{email}",
            'dealtechnologiescompany@gmail.com',
            ['Info@dealtecheg.com'],
        )

    
    return render(request,'temp/contactus.html',{})
