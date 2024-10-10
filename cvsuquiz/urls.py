from django.urls import path
from .views import quiz_home_view, BSESS_Quiz, BPED_Quiz, BSES_Quiz, cafenr_home_view



urlpatterns = [
   path('', quiz_home_view, name='quiz_home'),
   path('BSESS/', BSESS_Quiz, name='BSESS_quiz'),
   path('BPED/', BPED_Quiz, name='BPED_quiz'),
   path('BSES/', BSES_Quiz, name='BSES_quiz'),
   path('Cafenr/', cafenr_home_view, name='Cafenr_home'),
]