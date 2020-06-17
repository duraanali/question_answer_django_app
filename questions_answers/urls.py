from django.urls import path

from .views import questions_list, question_detail, answers_list

app_name = "questions"

urlpatterns = [
    path('', questions_list),
    path('answers/', answers_list),
    path('<id>/question_detail', question_detail),
]