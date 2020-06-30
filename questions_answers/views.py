from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Questions, Answers
from .forms import RegisterForm, askQuestion, AnswerQuestion, editQuestion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

def questions_list(request):
    
    # All Questions
    questions = Questions.objects.all().order_by('-created')
    
    # Search Function
    query = request.GET.get('q')
    if query:
        questions = questions.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(author__username__icontains=query)
            
            ).distinct()


    # Pagination of questions
    paginator = Paginator(questions, 3)  # 3 posts in each page
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
        
    
    context = {
        "questions_list": questions,
        'posts': posts,
        'page': page
    }
    
    return render(request, "questions.html", context)


def question_detail(request, id):
    singleQuestion = Questions.objects.get(id=id)
    
    answer = None
    # Reply Function
    if request.method == "POST":
        form = AnswerQuestion(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            question = get_object_or_404(Questions, id=id)
            print("question", question)
            answer.user = request.user
            answer.question_id = question
            answer.save()
            return HttpResponseRedirect("question_detail")
    else:
        form = AnswerQuestion(request.POST)
        
    # Number of Replies for 1 Question
    number_answers = Answers.objects.filter(question_id=id).count()
    print("nums of answers", number_answers)

    context = {
        "singleQuestion": singleQuestion,
        "number_answers": number_answers,
        "form": form
    }
    
    return render(request, "question_detail.html", context)

def answers_list(request, question_id):
    answer_count = Answers.objects.count(question_id=question_id)
    
    answers = Answers.objects.all().order_by('-created')
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




def delete_question(request, id=None):
    question_to_delete = Questions.objects.get(id=id)
    question_to_delete.delete()
    return HttpResponseRedirect('/')


def delete_reply(request, id=None):
    answer_to_delete = Answers.objects.get(id=id)
    answer_to_delete.delete()
    return HttpResponseRedirect('/')
    
    

def editCurrentQuestion(request, id=None):
    current_user = request.user
    question = Questions.objects.get(id=id, author=current_user)
    print("question", question)

    if request.method == 'POST':
        form = editQuestion(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = editQuestion(instance=question)
    else:
        form = editQuestion(instance=question)
        
    context = {'form': form, 'question': question}
    
    return render(request, 'edit_question.html', context)


def userInfo(request):
    logged_in_user = request.user
    logged_in_user_questions = Questions.objects.filter(author=logged_in_user).order_by('-created')
    logged_in_user_questions_num = Questions.objects.filter(author=logged_in_user).count()
    logged_in_user_answers_num = Answers.objects.filter(user=logged_in_user).count()
    
    print("logged_in_user_answers_num", logged_in_user_answers_num)
    current_user = request.user
    
    context = {
        "current_user": current_user,
        "logged_in_user_questions": logged_in_user_questions,
        "logged_in_user_questions_num": logged_in_user_questions_num,
        "logged_in_user_answers_num": logged_in_user_answers_num
    }
    return render(request, 'profile.html', context)


def user_questions(request):
    logged_in_user = request.user
    logged_in_user_posts = Questions.objects.filter(author=logged_in_user).order_by('-created')
    print("logged_in_user_posts", logged_in_user_posts)
    return render(request, 'profile.html', {'posts': logged_in_user_posts})
