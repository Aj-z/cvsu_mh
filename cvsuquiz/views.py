from django.shortcuts import render
from .forms import BsessQuiz, BpedQuiz, BsaQuiz, BsesQuiz, BaeQuiz, BsftQuiz, BsedQuiz, Bsed_EnglQuiz, Bsed_FiliQuiz, Bsed_MathQuiz, Bsed_ScieQuiz, Bsed_SoStQuiz

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

def cvmbs_home_view(request):
    return render(request, 'cvsuquiz/cvmbs.html')
# CED COURSES
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