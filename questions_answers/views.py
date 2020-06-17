from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Questions, Answers

def questions_list(request):
    questions = Questions.objects.all()
    context = {
        "questions_list": questions
    }
    return render(request, "questions.html", context)


def question_detail(request, id):
    question = Questions.objects.get(id=id)
    context = {
        "question": question
    }
    
    return render(request, "question_detail.html", context)

def answers_list(request):
    answers = Answers.objects.all()
    print(answers)
    context = {
        "answers": answers,
        }
    return render(request, 'answers.html', context)