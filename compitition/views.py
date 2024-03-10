from django.shortcuts import render
from . models import *
# questions list

def Questions_list(request):
    questions = Questions.objects.all()

    return render(request,'temp/competition.html',{'questions':questions})



# ansewer the questions

def Answer_question(request,slug):
    answer_question = Questions.objects.get(slug=slug)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        answer = request.POST['answer']
        
        new_answer = Answer(name=name,email=email,number=phone,answer=answer,question=answer_question )
        new_answer.save()

    return render(request,'temp/competition_details.html',{'ansewer_questions':answer_question})
     