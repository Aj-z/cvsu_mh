from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_home, name='quiz-home'),
    path('question/<int:question_id>/', views.question_view, name='question-view'),
]