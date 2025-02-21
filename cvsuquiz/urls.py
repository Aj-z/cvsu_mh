from django.urls import path
from .views import (cspear_home_view, BSESS_Quiz, BPED_Quiz, 
                    BSES_Quiz, cafenr_home_view, BSA_Quiz, 
                    BAE_Quiz, BSFT_Quiz, ced_home_view, 
                    BSE_ENGL_Quiz, BSE_FILI_Quiz, 
                    BSE_MATH_Quiz, BSE_SCIE_Quiz, 
                    BSE_SS_Quiz,BEED_Quiz,BSHM_Quiz,BSTM_Quiz,con_home_view, BSMT_QUIZ, BSM_QUIZ, BSN_QUIZ,
                    ceit_home_view,  
                    BSABE_QUIZ, BSARCH_QUIZ, BSCE_QUIZ, BSCpE_QUIZ, 
                    BSCS_QUIZ, BSEE_QUIZ, BSINDT_AT_QUIZ, BSINDT_ET_QUIZ,
                    BSINDT_EX_QUIZ, BSIT_QUIZ, BSOA_QUIZ, 
                    ccj_home_view,BSC_Quiz, cas_home_view, BAJ_QUIZ, 
                    BSE_ENGL_QUIZ,BAPS_QUIZ, BSAM_QUIZ, BSBIO_ANIMALBIO_QUIZ,
                    BSBIO_PLANTBIO_QUIZ, BSBIO_MICROBIO_QUIZ, BSBIO_MEDICALBIO_QUIZ,
                    BSBIO_ECOLOGY_QUIZ, BSBIO_GENETICS_QUIZ, BSPSYC_QUIZ, BSSW_QUIZ,
                    cvmbs_home_view,
                    cemds_home_view)



urlpatterns = [
    # ------  CSPEAR  ---------
   path('', cspear_home_view, name='CSPEAR_home'),
   path('BSESS/', BSESS_Quiz, name='BSESS_quiz'),
   path('BPED/', BPED_Quiz, name='BPED_quiz'),
   # ------  CAFENR  ---------
   path('CAFENR/', cafenr_home_view, name='CAFENR_home'),
   path('BSA/', BSA_Quiz, name='BSA_quiz'),
   path('BSES/', BSES_Quiz, name='BSES_quiz'),
   path('BAE/', BAE_Quiz, name='BAE_quiz'),
   path('BSFT/', BSFT_Quiz, name='BSFT_quiz'),
   # ------  CED  ---------
   path('CED/', ced_home_view, name='CED_home'),
   path('BSE-ENGL/', BSE_ENGL_Quiz, name='BSE-ENGL_quiz'),
   path('BSE-FILI/', BSE_FILI_Quiz, name='BSE-FILI_quiz'),
   path('BSE-MATH/', BSE_MATH_Quiz, name='BSE-MATH_quiz'),
   path('BSE-SCIE/', BSE_SCIE_Quiz, name='BSE-SCIE_quiz'),
   path('BSE-SS/', BSE_SS_Quiz, name='BSE-SS_quiz'),
   path('BEED/', BEED_Quiz, name='BEED_quiz'),
   path('BSHM/', BSHM_Quiz, name='BSHM_quiz'),
   path('BSTM/', BSTM_Quiz, name='BSTM_quiz'),

   # ------  CCJ  ---------
   path('CCJ/', ccj_home_view, name='CCJ_home'),
   path('BSC/', BSC_Quiz, name='BSC_quiz'), 
   # ------  CAS  ---------
   path('CAS/', cas_home_view, name='CAS_home'),
   path('BAJ/', BAJ_QUIZ, name='BAJ_quiz'),
   path('BSE_ENGL/', BSE_ENGL_QUIZ, name='BSE_ENGL_quiz'),
   path('BAPS_QUIZ/', BAPS_QUIZ, name='BAPS_QUIZ'),
   path('BSAM_QUIZ/', BSAM_QUIZ, name='BSAM_QUIZ'),
   path('BSBIO_ANIMALBIO_QUIZ/', BSBIO_ANIMALBIO_QUIZ, name='BSBIO_ANIMALBIO_QUIZ'),
   path('BSBIO_PLANTBIO_QUIZ/', BSBIO_PLANTBIO_QUIZ, name='BSBIO_PLANTBIO_QUIZ'),
   path('BSBIO_MICROBIO_QUIZ/', BSBIO_MICROBIO_QUIZ, name='BSBIO_MICROBIO_QUIZ'),
   path('BSBIO_MEDICALBIO_QUIZ/', BSBIO_MEDICALBIO_QUIZ, name='BSBIO_MEDICALBIO_QUIZ'),
   path('BSBIO_ECOLOGY_QUIZ/', BSBIO_ECOLOGY_QUIZ, name='BSBIO_ECOLOGY_QUIZ'),
   path('BSBIO_GENETICS_QUIZ/', BSBIO_GENETICS_QUIZ, name='BSBIO_GENETICS_QUIZ'),
   path('BSPSYC_QUIZ/', BSPSYC_QUIZ, name='BSPSYC_QUIZ'),
   path('BSSW_QUIZ/', BSSW_QUIZ, name='BSSW_QUIZ'),
    # ------  CON ---------
   path('CON/', con_home_view, name='CON_home'),
   path('BSMT_QUIZ/', BSMT_QUIZ, name='BSMT_quiz'),
   path('BSM_QUIZ/', BSM_QUIZ, name='BSM_quiz'),
   path('BSN_QUIZ/', BSN_QUIZ, name='BSN_quiz'),
   # ------  CEIT ---------
   path('CEIT/', ceit_home_view, name='CEIT_home'),
   path('BSABE_QUIZ/', BSABE_QUIZ, name='BSABE_quiz'),
   path('BSARCH_QUIZ/', BSARCH_QUIZ, name='BSARCH_quiz'),
   path('BSCE_QUIZ/', BSCE_QUIZ, name='BSCE_quiz'),
   path('BSCpE_QUIZ/', BSCpE_QUIZ, name='BSCpE_quiz'),
   path('BSCS_QUIZ/', BSCS_QUIZ, name='BSCS_quiz'),
   path('BSEE_QUIZ/', BSEE_QUIZ, name='BSEE_quiz'),
   path('BSINDT_AT_QUIZ/', BSINDT_AT_QUIZ, name='BSINDT-AT_quiz'),
   path('BSINDT_ET_QUIZ/', BSINDT_ET_QUIZ, name='BSINDT-ET_quiz'),
   path('BSINDT_EX_QUIZ', BSINDT_EX_QUIZ, name='BSINDT-EX_quiz'),
   path('BSIT_QUIZ/', BSIT_QUIZ, name='BSIT_quiz'),
   path('CEIT/', BSOA_QUIZ, name='BSOA_quiz'),
   # ------  CVMBS ---------
   path('CVMBS/', cvmbs_home_view, name='CVMBS_home'),
   # ------  CEMDS ---------
   path('CEMDS/', cemds_home_view, name='CEMDS_home'),
]