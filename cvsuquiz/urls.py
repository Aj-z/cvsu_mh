from django.urls import path
from .views import (cspear_home_view, BSESS_Quiz, BPED_Quiz, 
                    BSES_Quiz, cafenr_home_view, BSA_Quiz, 
                    BAE_Quiz, BSFT_Quiz, ced_home_view, 
                    BSE_ENGL_Quiz, BSE_FILI_Quiz, 
                    BSE_MATH_Quiz, BSE_SCIE_Quiz, 
                    BSE_SS_Quiz,con_home_view, ceit_home_view, 
                    ccj_home_view, cas_home_view, cvmbs_home_view,
                    cemds_home_view)



urlpatterns = [
   path('', cspear_home_view, name='CSPEAR_home'),
   path('BSESS/', BSESS_Quiz, name='BSESS_quiz'),
   path('BPED/', BPED_Quiz, name='BPED_quiz'),
   path('CAFENR/', cafenr_home_view, name='CAFENR_home'),
   path('BSA/', BSA_Quiz, name='BSA_quiz'),
   path('BSES/', BSES_Quiz, name='BSES_quiz'),
   path('BAE/', BAE_Quiz, name='BAE_quiz'),
   path('BSFT/', BSFT_Quiz, name='BSFT_quiz'),
   path('CED/', ced_home_view, name='CED_home'),
   path('BSE-ENGL/', BSE_ENGL_Quiz, name='BSE-ENGL_quiz'),
   path('BSE-FILI/', BSE_FILI_Quiz, name='BSE-FILI_quiz'),
   path('BSE-MATH/', BSE_MATH_Quiz, name='BSE-MATH_quiz'),
   path('BSE-SCIE/', BSE_SCIE_Quiz, name='BSE-SCIE_quiz'),
   path('BSE-SS/', BSE_SS_Quiz, name='BSE-SS_quiz'),
   path('CCJ/', ccj_home_view, name='CCJ_home'),
   path('CAS/', cas_home_view, name='CAS_home'),
   path('CON/', con_home_view, name='CON_home'),
   path('CEIT/', ceit_home_view, name='CEIT_home'),
   path('CVMBS/', cvmbs_home_view, name='CVMBS_home'),
   path('CEMDS/', cemds_home_view, name='CEMDS_home'),
]