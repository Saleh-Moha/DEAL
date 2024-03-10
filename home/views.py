from django.shortcuts import render
from . models import *
from django.core.mail import send_mail
def openingone(request):
    add = Openingone.objects.all()
    project = Projects.objects.all()
    opentow = Openingtow.objects.all()
    openthree = Openingthree.objects.all()
    
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
    
    context={'add':add,'projects':project , 'addtow':opentow,'addthree':openthree}
    return render (request,'temp/index.html',context)



# projects 

# def add_projects(request):
#     project = Projects.objects.all()

#     context={'projects':project}
#     return render (request,'temp/index.html',context)  
    