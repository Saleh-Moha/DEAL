from django.shortcuts import render
from django.core.mail import send_mail
def servc(request):
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
    return render(request,'temp/service.html',{})
