from django.urls import path
from .views import quiz_home_view, quiz_home



urlpatterns = [
   path('', quiz_home_view, name='quiz_home'),
   path('cspear/', quiz_home, name='cspear_quiz'),
]