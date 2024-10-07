from django.urls import path
from .views import quiz_home_view, quiz_home, BPED_Quiz



urlpatterns = [
   path('', quiz_home_view, name='quiz_home'),
   path('cspear/', quiz_home, name='cspear_quiz'),
   path('BPED/', BPED_Quiz, name='BPED_quiz'),
]