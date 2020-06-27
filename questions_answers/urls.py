from django.urls import path, include

from .views import (
    questions_list, 
    question_detail, 
    allUsers, 
    register, 
    newQuestion, 
    editQuestion, 
    delete_question, 
    userInfo,
    user_questions
)


app_name = "questions"

urlpatterns = [
    path('', questions_list),
    path('register/', register, name="register"),
    path('allusers/', allUsers),
    path('ask_question/', newQuestion),
    path('profile/', userInfo),
    path('user_questions/', user_questions),
    path('<id>/edit_question', editQuestion),
    path('', include("django.contrib.auth.urls")),
    path('<id>/question_detail', question_detail),
    path('tinymce/', include('tinymce.urls')),
    path('question/<int:id>/delete/', delete_question, name='delete_question'),
]
