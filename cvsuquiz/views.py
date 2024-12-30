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
    College_Name = "College of Art And Sciences"
    Carousel_1img ="https://images.pexels.com/photos/29846183/pexels-photo-29846183/free-photo-of-newspapers-on-display-in-istanbul-street.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1 "
    Carousel_1h5="Journalism is what maintains democracy. It's the force for progressive social change."
    Carousel_1p="-Andrew Vachss"
    Carousel_2img ="https://images.pexels.com/photos/4057663/pexels-photo-4057663.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="The job of the newspaper is to comfort the afflicted and afflict the comfortable."
    Carousel_2p="-Finley Peter Dunne"
    Carousel_3img ="https://images.pexels.com/photos/16077108/pexels-photo-16077108/free-photo-of-hand-holding-turkish-newspaper.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="Put it before them briefly so they will read it, clearly so they will appreciate it, picturesquely so they will remember it, and, above all, accurately so they will be guided by its light."
    Carousel_3p="-Joseph Pulitzer"


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
       'College_Name': College_Name,
       'Carousel_1img': Carousel_1img,
       'Carousel_1h5' : Carousel_1h5,
        'Carousel_1p' : Carousel_1p,
        'Carousel_2img' : Carousel_2img,
        'Carousel_2h5' : Carousel_2h5,
        'Carousel_2p' : Carousel_2p,
        'Carousel_3img' : Carousel_3img,
        'Carousel_3h5' : Carousel_3h5,
        'Carousel_3p' : Carousel_3p,
    })
def BSE_ENGL_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Arts in English Language Studies"
    College_Name = "College of Art And Sciences"
    Carousel_1img ="https://images.pexels.com/photos/11954971/pexels-photo-11954971.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="A word after a word after a word is power"
    Carousel_1p="- Margaret Atwood"
    Carousel_2img ="https://images.pexels.com/photos/5929346/pexels-photo-5929346.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Reading maketh a full man; conference a ready man; and writing an exact man."
    Carousel_2p="- Francis Bacon"
    Carousel_3img ="https://images.pexels.com/photos/3700658/pexels-photo-3700658.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="The humanities are not a luxury. They reflect the creativity of a free society."
    Carousel_3p="- Drew Gilpin Faust"


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
        'College_Name': College_Name,
       'Carousel_1img': Carousel_1img,
       'Carousel_1h5' : Carousel_1h5,
        'Carousel_1p' : Carousel_1p,
        'Carousel_2img' : Carousel_2img,
        'Carousel_2h5' : Carousel_2h5,
        'Carousel_2p' : Carousel_2p,
        'Carousel_3img' : Carousel_3img,
        'Carousel_3h5' : Carousel_3h5,
        'Carousel_3p' : Carousel_3p,
    })
def BAPS_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Arts in Political Science"
    College_Name = "College of Art And Sciences"
    Carousel_1img ="https://images.pexels.com/photos/5669619/pexels-photo-5669619.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="The care of human life and happiness, and not their destruction, is the first and only object of good government."
    Carousel_1p="- Thomas Jefferson"
    Carousel_2img ="https://images.pexels.com/photos/15686925/pexels-photo-15686925/free-photo-of-wiener-justizpalast.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="A leader is best when people barely know he exists, when his work is done, his aim fulfilled, they will say: We did it ourselves."
    Carousel_2p="- Lao Tzu"
    Carousel_3img ="https://images.pexels.com/photos/8112195/pexels-photo-8112195.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="Those who deny freedom to others deserve it not for themselves"
    Carousel_3p="- Abraham Lincoln"


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
        'College_Name': College_Name,
       'Carousel_1img': Carousel_1img,
       'Carousel_1h5' : Carousel_1h5,
        'Carousel_1p' : Carousel_1p,
        'Carousel_2img' : Carousel_2img,
        'Carousel_2h5' : Carousel_2h5,
        'Carousel_2p' : Carousel_2p,
        'Carousel_3img' : Carousel_3img,
        'Carousel_3h5' : Carousel_3h5,
        'Carousel_3p' : Carousel_3p,
    })
def BSAM_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Applied Mathematics"
    College_Name = "College of Art And Sciences"
    Carousel_1img ="https://images.pexels.com/photos/4778677/pexels-photo-4778677.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Without mathematics, there's nothing you can do. Everything around you is mathematics. Everything around you is numbers."
    Carousel_1p="- Shakuntala Devi"
    Carousel_2img ="https://images.pexels.com/photos/6238297/pexels-photo-6238297.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Mathematics knows no races or geographic boundaries; for mathematics, the cultural world is one country."
    Carousel_2p="- David Hilbert"
    Carousel_3img ="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Einstein_1921_by_F_Schmutzer_-_restoration.jpg/585px-Einstein_1921_by_F_Schmutzer_-_restoration.jpg"
    Carousel_3h5="Pure mathematics is, in its way, the poetry of logical ideas."
    Carousel_3p="- Albert Einstein"
    


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
        'College_Name': College_Name,
       'Carousel_1img': Carousel_1img,
       'Carousel_1h5' : Carousel_1h5,
        'Carousel_1p' : Carousel_1p,
        'Carousel_2img' : Carousel_2img,
        'Carousel_2h5' : Carousel_2h5,
        'Carousel_2p' : Carousel_2p,
        'Carousel_3img' : Carousel_3img,
        'Carousel_3h5' : Carousel_3h5,
        'Carousel_3p' : Carousel_3p,
        
    })
def BSBIO_ANIMALBIO_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Biology, Major in Animal Biology"
    College_Name = "College of Art And Sciences"
    Carousel_1img ="https://images.pexels.com/photos/2671074/pexels-photo-2671074.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Nothing in biology makes sense except in the light of evolution."
    Carousel_1p="- Theodosius Dobzhansky"
    Carousel_2img ="https://images.pexels.com/photos/16141023/pexels-photo-16141023/free-photo-of-close-up-of-a-baby-monkey.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="If we study the lives of animals, we learn more about ourselves"
    Carousel_2p="- Jane Goodall"
    Carousel_3img ="https://images.pexels.com/photos/19916617/pexels-photo-19916617/free-photo-of-two-marine-iguanas-sitting-on-a-rocky-surface.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="The more clearly we can focus our attention on the wonders and realities of the universe about us, the less taste we shall have for destruction."
    Carousel_3p="-  Rachel Carson"


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
        'College_Name': College_Name,
        'Carousel_1img': Carousel_1img,
        'Carousel_1h5' : Carousel_1h5,
        'Carousel_1p' : Carousel_1p,
        'Carousel_2img' : Carousel_2img,
        'Carousel_2h5' : Carousel_2h5,
        'Carousel_2p' : Carousel_2p,
        'Carousel_3img' : Carousel_3img,
        'Carousel_3h5' : Carousel_3h5,
        'Carousel_3p' : Carousel_3p,
    })
def BSBIO_PLANTBIO_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Biology, Major in Plant Biology"
    College_Name = "College of Art And Sciences"
    Carousel_1img ="https://images.pexels.com/photos/797793/pexels-photo-797793.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="The world is green because plants produce chlorophyll, the foundation of the food web."
    Carousel_1p="- Carl Linnaeus"
    Carousel_2img ="https://images.pexels.com/photos/7718273/pexels-photo-7718273.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="It is not the strongest of the species that survive, nor the most intelligent, but the one most responsive to change."
    Carousel_2p="- Charles Darwin"
    Carousel_3img ="https://images.pexels.com/photos/4608993/pexels-photo-4608993.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="Look deep into nature, and then you will understand everything better."
    Carousel_3p="- Albert Einstein"
    


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
        'College_Name': College_Name,
        'Carousel_1img': Carousel_1img,
        'Carousel_1h5' : Carousel_1h5,
        'Carousel_1p' : Carousel_1p,
        'Carousel_2img' : Carousel_2img,
        'Carousel_2h5' : Carousel_2h5,
        'Carousel_2p' : Carousel_2p,
        'Carousel_3img' : Carousel_3img,
        'Carousel_3h5' : Carousel_3h5,
        'Carousel_3p' : Carousel_3p,
        
    })
def BSBIO_MICROBIO_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Biology, Major in Microbiology"
    College_Name = "College of Art And Sciences"
    Carousel_1img ="https://images.pexels.com/photos/13966056/pexels-photo-13966056.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Life would be impossible without microbes."
    Carousel_1p="- Carl Woese"
    Carousel_2img ="https://images.pexels.com/photos/4031365/pexels-photo-4031365.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Microbes are doing things we didn’t think they could do—they’re both the powerhouses and protectors of ecosystems"
    Carousel_2p="- Rita Colwell"
    Carousel_3img ="https://images.pexels.com/photos/6203349/pexels-photo-6203349.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="Biology gives you a brain. Life turns it into a mind."
    Carousel_3p="- Jeffrey Eugenides"


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
        'College_Name': College_Name,
        'Carousel_1img': Carousel_1img,
        'Carousel_1h5' : Carousel_1h5,
        'Carousel_1p' : Carousel_1p,
        'Carousel_2img' : Carousel_2img,
        'Carousel_2h5' : Carousel_2h5,
        'Carousel_2p' : Carousel_2p,
        'Carousel_3img' : Carousel_3img,
        'Carousel_3h5' : Carousel_3h5,
        'Carousel_3p' : Carousel_3p,
    })
def BSBIO_MEDICALBIO_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = " Bachelor of Science in Biology, Major in Medical Biology"
    College_Name = "College of Art And Sciences"
    Carousel_1img ="https://images.pexels.com/photos/3912365/pexels-photo-3912365.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Medicine is a science of uncertainty and an art of probability."
    Carousel_1p="- William Osler"
    Carousel_2img ="https://images.pexels.com/photos/3825578/pexels-photo-3825578.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="In the fields of observation, chance favors only the prepared mind"
    Carousel_2p="-  Louis Pasteur"
    Carousel_3img ="https://images.pexels.com/photos/2678059/pexels-photo-2678059.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="It is far more important to know what person the disease has than what disease the person has"
    Carousel_3p="- Hippocrates"


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
        'College_Name': College_Name,
        'Carousel_1img': Carousel_1img,
        'Carousel_1h5' : Carousel_1h5,
        'Carousel_1p' : Carousel_1p,
        'Carousel_2img' : Carousel_2img,
        'Carousel_2h5' : Carousel_2h5,
        'Carousel_2p' : Carousel_2p,
        'Carousel_3img' : Carousel_3img,
        'Carousel_3h5' : Carousel_3h5,
        'Carousel_3p' : Carousel_3p,
    })
def BSBIO_ECOLOGY_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Biology, Major in Ecology"
    College_Name = "College of Art And Sciences"
    Carousel_1img ="https://images.pexels.com/photos/29958398/pexels-photo-29958398/free-photo-of-macro-shot-of-hoverfly-on-celosia-flower.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="We abuse land because we regard it as a commodity belonging to us. When we see land as a community to which we belong, we may begin to use it with love and respect."
    Carousel_1p="- Aldo Leopold"
    Carousel_2img ="https://images.pexels.com/photos/1466434/pexels-photo-1466434.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Man shapes himself through decisions that shape his environment."
    Carousel_2p="-  René Dubos"
    Carousel_3img ="https://images.pexels.com/photos/2319029/pexels-photo-2319029.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="The Earth is what we all have in common."
    Carousel_3p="- Wendell Berry"


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
        'College_Name': College_Name,
        'Carousel_1img': Carousel_1img,
        'Carousel_1h5' : Carousel_1h5,
        'Carousel_1p' : Carousel_1p,
        'Carousel_2img' : Carousel_2img,
        'Carousel_2h5' : Carousel_2h5,
        'Carousel_2p' : Carousel_2p,
        'Carousel_3img' : Carousel_3img,
        'Carousel_3h5' : Carousel_3h5,
        'Carousel_3p' : Carousel_3p,
    })
def BSBIO_GENETICS_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Biology, Major in Genetics"
    College_Name = "College of Art And Sciences"
    Carousel_1img ="https://images.pexels.com/photos/15685385/pexels-photo-15685385/free-photo-of-sunlight-on-a-blue-eye.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="It requires indeed some courage to undertake a labor of such far-reaching extent; but the results of an entire life often hang on a single card"
    Carousel_1p="- Gregor Mendel"
    Carousel_2img ="https://images.pexels.com/photos/7202960/pexels-photo-7202960.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="We used to think our fate was in the stars. Now we know, in large measure, our fate is in our genes."
    Carousel_2p="-  James Watson"
    Carousel_3img ="https://images.pexels.com/photos/3825379/pexels-photo-3825379.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="The ultimate aim of the modern movement in biology is to explain all biology in terms of physics and chemistry"
    Carousel_3p="- Francis Crick"


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
        'College_Name': College_Name,
        'Carousel_1img': Carousel_1img,
        'Carousel_1h5' : Carousel_1h5,
        'Carousel_1p' : Carousel_1p,
        'Carousel_2img' : Carousel_2img,
        'Carousel_2h5' : Carousel_2h5,
        'Carousel_2p' : Carousel_2p,
        'Carousel_3img' : Carousel_3img,
        'Carousel_3h5' : Carousel_3h5,
        'Carousel_3p' : Carousel_3p,
    })
def BSPSYC_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Psychology"
    College_Name = "College of Art And Sciences"
    Carousel_1img ="https://images.pexels.com/photos/20433653/pexels-photo-20433653/free-photo-of-close-up-of-a-pinocchio-wooden-puppet.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Being entirely honest with oneself is a good exercise"
    Carousel_1p="- Sigmund Freud"
    Carousel_2img ="https://images.pexels.com/photos/885880/pexels-photo-885880.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="The privilege of a lifetime is to become who you truly are."
    Carousel_2p="-Carl Jung"
    Carousel_3img ="https://images.pexels.com/photos/6249474/pexels-photo-6249474.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="The curious paradox is that when I accept myself just as I am, then I can change."
    Carousel_3p="- Carl Rogers"


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
        'College_Name': College_Name,
        'Carousel_1img': Carousel_1img,
        'Carousel_1h5' : Carousel_1h5,
        'Carousel_1p' : Carousel_1p,
        'Carousel_2img' : Carousel_2img,
        'Carousel_2h5' : Carousel_2h5,
        'Carousel_2p' : Carousel_2p,
        'Carousel_3img' : Carousel_3img,
        'Carousel_3h5' : Carousel_3h5,
        'Carousel_3p' : Carousel_3p,
    })
def BSSW_QUIZ(request):
    css_style = "cas.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Social Work"
    College_Name = "College of Art And Sciences"
    Carousel_1img ="https://images.pexels.com/photos/5710994/pexels-photo-5710994.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="The good we secure for ourselves is precarious and uncertain until it is secured for all of us and incorporated into our common life."
    Carousel_1p="- Jane Addams"
    Carousel_2img ="https://images.pexels.com/photos/6646816/pexels-photo-6646816.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Without community service, we would not have a strong quality of life. It’s important to the person who serves as well as the recipient. It’s the way in which we ourselves grow and develop."
    Carousel_2p=" - Dorothy Height"
    Carousel_3img ="https://images.pexels.com/photos/6591155/pexels-photo-6591155.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5=" Social justice is the great work of our generation. It is the moral obligation of those with the capacity to help, to do so."
    Carousel_3p="- Whitney M. Young Jr."


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
        'College_Name': College_Name,
        'Carousel_1img': Carousel_1img,
        'Carousel_1h5' : Carousel_1h5,
        'Carousel_1p' : Carousel_1p,
        'Carousel_2img' : Carousel_2img,
        'Carousel_2h5' : Carousel_2h5,
        'Carousel_2p' : Carousel_2p,
        'Carousel_3img' : Carousel_3img,
        'Carousel_3h5' : Carousel_3h5,
        'Carousel_3p' : Carousel_3p,
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