from django.urls import path, include

from .views import (
    questions_list, 
    question_detail, 
    allUsers, 
    register, 
    newQuestion, 
    editCurrentQuestion,
    delete_question, 
    userInfo,
    user_questions,
    answers_list,
    delete_reply
)


app_name = "questions"

urlpatterns = [
    path('', questions_list),
    path('register/', register, name="register"),
    path('allusers/', allUsers),
    path('ask_question/', newQuestion),
    path('answers/', answers_list),
    path('profile/', userInfo),
    path('user_questions/', user_questions),
    path('<id>/edit_question', editCurrentQuestion),
    path('', include("django.contrib.auth.urls")),
    path('<id>/question_detail', question_detail, name="question_detail"),
    path('tinymce/', include('tinymce.urls')),
    path('<id>/delete_question', delete_question),
    path('<id>/delete_reply', delete_reply),
]
