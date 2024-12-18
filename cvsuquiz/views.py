from django.shortcuts import render
from .forms import (BsessQuiz, BpedQuiz, BsaQuiz, 
                    BsesQuiz, BaeQuiz, BsftQuiz, Bsed_EnglQuiz, 
                    Bsed_FiliQuiz, Bsed_MathQuiz, Bsed_ScieQuiz,
                    Bsed_SoStQuiz, BajQuiz, BSE_ENGLQuiz, BAPSQuiz, 
                    BSAMQuiz, BSBIO_ANIMALBIO_Quiz, BSBIO_PLANTBIO_Quiz, 
                    BSBIO_MICROBIO_Quiz, BSBIO_MEDICALBIO_Quiz, BSBIO_ECOLOGY_Quiz,
                    BSBIO_ECOLOGY_Quiz, BSBIO_GENETICS_Quiz, BSBIO_GENETICS_Quiz,
                    BSPSYC_Quiz, BSSW_Quiz)

# ------  CSPEAR  ---------
def cspear_home_view(request):
    return render(request, 'cvsuquiz/Cspear.html')


def BSESS_Quiz(request):
    COURSE_NAME = "Bachelor of Science in Exercise and Sports Sciences"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None



    if request.method == "POST":
        form = BsessQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '1':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is A"

            if answer_q2 == '2':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is B"

            if answer_q3 == '4':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is D"    
    else:
        form = BsessQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
    })
def BPED_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Physical Education"


    if request.method == "POST":
        form = BpedQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '3':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is C"

            if answer_q2 == '2':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is B"

            if answer_q3 == '2':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is B"    
    else:
        form = BpedQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
    })

# ------  CAFENR  ---------
def cafenr_home_view(request):
    return render(request, 'cvsuquiz/cafenr.html')

def BSA_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor Of Science In Agriculture"


    if request.method == "POST":
        form = BsaQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '3':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is C"

            if answer_q2 == '3':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is C"

            if answer_q3 == '4':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is D"    
    else:
        form = BsaQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
    })
def BAE_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor in Agricultural Technology"


    if request.method == "POST":
        form = BaeQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '1':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is A"

            if answer_q2 == '3':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is C"

            if answer_q3 == '3':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is C"    
    else:
        form = BaeQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
    })
def BSES_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science In Environmental Science"


    if request.method == "POST":
        form = BsesQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '2':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is B"

            if answer_q3 == '2':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is B"    
    else:
        form = BsesQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
    })
def BSFT_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science In Food Technology"


    if request.method == "POST":
        form = BsftQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '1':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is A"

            if answer_q3 == '2':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is B"    
    else:
        form = BsftQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
    })

# ------  CVMBS  ---------
def cvmbs_home_view(request):
    return render(request, 'cvsuquiz/cvmbs.html')

# ------  CED  ---------
def ced_home_view(request):
    return render(request, 'cvsuquiz/ced.html')
  # Bachelor of Secondary Education Majors
def BSE_ENGL_Quiz(request):
    css_style = "ced.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Secondary Education Major In English"


    if request.method == "POST":
        form = Bsed_EnglQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '3':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is C"

            if answer_q2 == '2':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is B"

            if answer_q3 == '3':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is C"    
    else:
        form = Bsed_EnglQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
        'css_style' : css_style,
    })
def BSE_FILI_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Secondary Education Major In Filipino"


    if request.method == "POST":
        form = Bsed_FiliQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '1':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is A"

            if answer_q3 == '1':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is A"    
    else:
        form = Bsed_FiliQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
    })
def BSE_MATH_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Secondary Education Major In Math"


    if request.method == "POST":
        form = Bsed_MathQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '2':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is B"

            if answer_q3 == '2':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is B"    
    else:
        form = Bsed_MathQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
    })
def BSE_SCIE_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Secondary Education Major In Science"


    if request.method == "POST":
        form = Bsed_ScieQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '3':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is C"

            if answer_q3 == '3':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is C"    
    else:
        form = Bsed_ScieQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
    })
def BSE_SS_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Secondary Education Major In Social Studies"


    if request.method == "POST":
        form = Bsed_SoStQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '2':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is B"

            if answer_q3 == '3':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is C"    
    else:
        form = Bsed_SoStQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
    })

def BEED_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor in Agricultural Technology"


    if request.method == "POST":
        form = BaeQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '1':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is A"

            if answer_q2 == '3':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is C"

            if answer_q3 == '3':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is C"    
    else:
        form = BaeQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
    })
def BSHRM_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science In Environmental Science"


    if request.method == "POST":
        form = BsesQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '2':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is B"

            if answer_q3 == '2':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is B"    
    else:
        form = BsesQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
    })
def BSTM_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science In Environmental Science"


    if request.method == "POST":
        form = BsesQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '2':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is B"

            if answer_q3 == '2':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is B"    
    else:
        form = BsesQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
    })


# ------  CCJ ---------
def ccj_home_view(request):
    return render(request, 'cvsuquiz/ccj.html')

# ------  CAS ---------
def cas_home_view(request):
    return render(request, 'cvsuquiz/cas.html')
def BAJ_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Arts in Journalism"


    if request.method == "POST":
        form = BajQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '1':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is A"

            if answer_q3 == '3':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is C"    
    else:
        form = BajQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
        'css_style' : css_style,
    })
def BSE_ENGL_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Arts in English Language Studies"


    if request.method == "POST":
        form = BSE_ENGLQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '2':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is B"

            if answer_q3 == '3':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is C"    
    else:
        form = BSE_ENGLQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
        'css_style' : css_style,
    })
def BAPS_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Arts in Political Science"


    if request.method == "POST":
        form = BAPSQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '2':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is B"

            if answer_q3 == '3':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is C"    
    else:
        form = BAPSQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
        'css_style' : css_style,
    })
def BSAM_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Applied Mathematics"


    if request.method == "POST":
        form = BSAMQuiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '1':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is A"

            if answer_q2 == '1':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is A"

            if answer_q3 == '1':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is A"    
    else:
        form = BSAMQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
        'css_style' : css_style,
    })
def BSBIO_ANIMALBIO_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Biology, Major in Animal Biology"


    if request.method == "POST":
        form = BSBIO_ANIMALBIO_Quiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '3':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is C"

            if answer_q2 == '2':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is B"

            if answer_q3 == 'B':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is B"    
    else:
        form = BSBIO_ANIMALBIO_Quiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
        'css_style' : css_style,
    })
def BSBIO_PLANTBIO_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Biology, Major in Plant Biology"


    if request.method == "POST":
        form = BSBIO_PLANTBIO_Quiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '3':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is C"

            if answer_q2 == '3':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is C"

            if answer_q3 == '4':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is D"    
    else:
        form = BSBIO_PLANTBIO_Quiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
        'css_style' : css_style,
    })
def BSBIO_MICROBIO_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Biology, Major in Microbiology"


    if request.method == "POST":
        form = BSBIO_MICROBIO_Quiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '3':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is C"

            if answer_q2 == '3':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is C"

            if answer_q3 == '2':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is B"    
    else:
        form = BSBIO_MICROBIO_Quiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
        'css_style' : css_style,
    })
def BSBIO_MEDICALBIO_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = " Bachelor of Science in Biology, Major in Medical Biology"


    if request.method == "POST":
        form = BSBIO_MEDICALBIO_Quiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '2':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is B"

            if answer_q3 == '3':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is C"    
    else:
        form = BSBIO_MEDICALBIO_Quiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
        'css_style' : css_style,
    })
def BSBIO_ECOLOGY_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Biology, Major in Ecology"


    if request.method == "POST":
        form = BSBIO_ECOLOGY_Quiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '2':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is B"

            if answer_q3 == '2':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is B"    
    else:
        form = BSBIO_ECOLOGY_Quiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
        'css_style' : css_style,
    })
def BSBIO_GENETICS_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Biology, Major in Genetics"


    if request.method == "POST":
        form = BSBIO_GENETICS_Quiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '2':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is B"

            if answer_q3 == 'B':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is B"    
    else:
        form = BSBIO_GENETICS_Quiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
        'css_style' : css_style,
    })
def BSPSYC_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Psychology"


    if request.method == "POST":
        form = BSPSYC_Quiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '3':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is C"

            if answer_q3 == '2':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is B"    
    else:
        form = BSPSYC_Quiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
        'css_style' : css_style,
    })
def BSSW_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Social Work"


    if request.method == "POST":
        form = BSSW_Quiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '2':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is B"

            if answer_q2 == '3':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is C"

            if answer_q3 == '2':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is B"    
    else:
        form = BSSW_Quiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'COURSE_NAME': COURSE_NAME,
        'css_style' : css_style,
    })

# ------  CON ---------
def con_home_view(request):
    return render(request, 'cvsuquiz/con.html')

# ------  CEIT ---------
def ceit_home_view(request):
    return render(request, 'cvsuquiz/ceit.html')

# ------  CEIT ---------
def cemds_home_view(request):
    return render(request, 'cvsuquiz/cemds.html')