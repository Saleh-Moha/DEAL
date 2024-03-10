from django.shortcuts import render
from . models import *
from django.core.mail import send_mail
# Blog

def blog_list(request):
    list = Blog.objects.all()
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
    return render(request,'temp/Blog.html',{'lists':list})


# blog details

def blog_details(request,slug):
    detail = Blog.objects.get(Slug=slug)
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
    return render(request,'temp/Blog_details.html',{'details':detail})