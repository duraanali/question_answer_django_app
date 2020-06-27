from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Questions, Answers
from .forms import RegisterForm, askQuestion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

def questions_list(request):
    question_count = Questions.objects.count()
    questions = Questions.objects.all().order_by('-created')
    answers_count_for_question = Answers.objects.filter().count()
    query = request.GET.get('q')
    if query:
        questions = questions.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(author__username__icontains=query)
            
            ).distinct()
    print("answers_count", answers_count_for_question)
    context = {
        "questions_list": questions,
        "question_count": question_count
    }
    return render(request, "questions.html", context)


def question_detail(request, id):
    question = Questions.objects.get(id=id)
    answers_count = Answers.objects.filter().count()
    context = {
        "question": question
    }
    
    return render(request, "question_detail.html", context)

def answers_list(request, question_id):
    answer_count = Answers.objects.count(question_id=question_id)
    answers = Answers.objects.all()
    print("answer", answers.reply)
    context = {
        "answers": answers,
        "answer_count": answer_count
        }
    return render(request, 'answers.html', context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = RegisterForm()
    
    context = {
        "form":form
    }
   
    return render(request, "register.html", context)


def allUsers(response):
    print("users", response)
    return render(response, "register.html", {})


def newQuestion(request):
    template = 'ask_question.html'
    form = askQuestion(request.POST or None)

    if form.is_valid():
        
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        
        return redirect("/")
    else:
        form = askQuestion()
    
    context = {
        'form': form
    }

    return render(request, template, context)


def delete_question(request, id):
    question = get_object_or_404(askQuestion, id=id)
    print("question deleted", question)
    question.delete()
    return redirect('/')
    
    
@login_required(login_url='/')
def editQuestion(request, id):
    question = Questions.objects.get(id=id, author=request.user)
    
    if request.method == 'POST':
        form = askQuestion(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = askQuestion(instance=question)
    else:
        form = askQuestion(instance=question)
    return render(request, 'edit_question.html', {'form': form, 'question': question})


def userInfo(request):
    logged_in_user = request.user
    logged_in_user_questions = Questions.objects.filter(author=logged_in_user).order_by('-created')
    logged_in_user_questions = Questions.objects.filter(author=logged_in_user).order_by('-created')
    current_user = request.user
    context = {
        "current_user": current_user,
        "logged_in_user_questions": logged_in_user_questions
    }
    return render(request, 'profile.html', context)


def user_questions(request):
    logged_in_user = request.user
    logged_in_user_posts = Questions.objects.filter(author=logged_in_user).order_by('-created')
    print("logged_in_user_posts", logged_in_user_posts)
    return render(request, 'profile.html', {'posts': logged_in_user_posts})
