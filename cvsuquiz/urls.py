from django.urls import path
from .views import quiz_home_view, BSESS_Quiz, BPED_Quiz, BSES_Quiz, cafenr_home_view, BSA_Quiz, BAE_Quiz, BSFT_Quiz, ced_home_view, BSE_ENGL_Quiz, BSE_FILI_Quiz, BSE_MATH_Quiz, BSE_SCIE_Quiz, BSE_SS_Quiz



urlpatterns = [
   path('', quiz_home_view, name='quiz_home'),
   path('BSESS/', BSESS_Quiz, name='BSESS_quiz'),
   path('BPED/', BPED_Quiz, name='BPED_quiz'),
   path('Cafenr/', cafenr_home_view, name='Cafenr_home'),
   path('BSA/', BSA_Quiz, name='BSA_quiz'),
   path('BSES/', BSES_Quiz, name='BSES_quiz'),
   path('BAE/', BAE_Quiz, name='BAE_quiz'),
   path('BSFT/', BSFT_Quiz, name='BSFT_quiz'),
   path('Ced/', ced_home_view, name='Ced_home'),
   path('BSE-ENGL/', BSE_ENGL_Quiz, name='BSE-ENGL_quiz'),
   path('BSE-FILI/', BSE_FILI_Quiz, name='BSE-FILI_quiz'),
   path('BSE-MATH/', BSE_MATH_Quiz, name='BSE-MATH_quiz'),
   path('BSE-SCIE/', BSE_SCIE_Quiz, name='BSE-SCIE_quiz'),
   path('BSE-SS/', BSE_SS_Quiz, name='BSE-SS_quiz'),
]