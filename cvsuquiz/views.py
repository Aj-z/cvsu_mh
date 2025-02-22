from django.shortcuts import render
from django.urls import reverse
from .forms import (BsessQuiz, BpedQuiz, BsaQuiz, 
                    BsesQuiz, BaeQuiz, BsftQuiz, Bsed_EnglQuiz, 
                    Bsed_FiliQuiz, Bsed_MathQuiz, Bsed_ScieQuiz,
                    Bsed_SoStQuiz,BEEDQuiz,BSHMQuiz,BSTMQuiz, BajQuiz, BSE_ENGLQuiz, BAPSQuiz, 
                    BSAMQuiz, BSBIO_ANIMALBIO_Quiz, BSBIO_PLANTBIO_Quiz, 
                    BSBIO_MICROBIO_Quiz, BSBIO_MEDICALBIO_Quiz, BSBIO_ECOLOGY_Quiz,
                    BSBIO_ECOLOGY_Quiz, BSBIO_GENETICS_Quiz, BSBIO_GENETICS_Quiz,
                    BSPSYC_Quiz, BSSW_Quiz, BSABE_Quiz, BSARCH_Quiz, BSCE_Quiz, 
                    BSCpE_Quiz, BSCS_Quiz, BSEE_Quiz, BSINDT_AT_Quiz, 
                    BSINDT_ET_Quiz, BSINDT_EX_Quiz, BSIT_Quiz, BSOA_Quiz,
                    BSMT_Quiz, BSM_Quiz, BSN_Quiz,BSCQuiz)

# ------  CSPEAR  ---------
def cspear_home_view(request):
    return render(request, 'cvsuquiz/Cspear.html')


def BSESS_Quiz(request):
    COURSE_NAME = "Bachelor of Science in Exercise and Sports Sciences"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    css_style = "cspear.css"
    College_Name = "College of Sports, Physical Education and Recreation"
    Carousel_1img ="https://images.pexels.com/photos/30617264/pexels-photo-30617264/free-photo-of-exciting-hockey-game-at-delta-center-arena.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Sport has the power to change the world. It has the power to inspire. It has the power to unite people in a way that little else does."
    Carousel_1p="-Nelson Mandela"
    Carousel_2img ="https://images.pexels.com/photos/159607/basketball-player-girls-basketball-girl-159607.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Sport is part of every man and woman’s heritage and its absence can never be compensated for."
    Carousel_2p="-Pierre de Coubertin"
    Carousel_3img ="https://images.pexels.com/photos/159515/football-american-football-runner-player-159515.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="The man who can drive himself further once the effort gets painful is the man who will win."
    Carousel_3p="-Roger Bannister"
    Go_back=reverse('CSPEAR_home')



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
        'Go_back': Go_back
    })
def BPED_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Physical Education"
    css_style = "cspear.css"
    College_Name = "College of Sports, Physical Education and Recreation"
    Carousel_1img ="https://images.pexels.com/photos/8537187/pexels-photo-8537187.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Intelligence and skill can only function at the peak of their capacity when the body is healthy and strong."
    Carousel_1p="- John F. Kennedy "
    Carousel_2img ="https://images.pexels.com/photos/15138028/pexels-photo-15138028/free-photo-of-boy-during-pe-classes.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="The education of the body must precede that of the intellect."
    Carousel_2p="-Aristotle"
    Carousel_3img ="https://images.pexels.com/photos/8430349/pexels-photo-8430349.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="A sound mind in a sound body is a short but full description of a happy state in this world."
    Carousel_3p="-Friedrich Ludwig Jahn"
    Go_back=reverse('CSPEAR_home')
    


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
        'Go_back': Go_back
    })

# ------  CAFENR  ---------
def cafenr_home_view(request):
    return render(request, 'cvsuquiz/cafenr.html')

def BSA_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor Of Science In Agriculture"
    css_style = "cafenr.css"
    College_Name = "College Of Agriculture, Forestry, Environment and Natural Resources"
    Carousel_1img ="https://images.pexels.com/photos/10039946/pexels-photo-10039946.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Agriculture not only gives riches to a nation but the only riches she can call her own."
    Carousel_1p="-Samuel Johnson"
    Carousel_2img ="https://images.pexels.com/photos/10041309/pexels-photo-10041309.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="The farmer is the only man in our economy who buys everything at retail, sells everything at wholesale, and pays the freight both ways."
    Carousel_2p="-John F. Kennedy"
    Carousel_3img ="https://images.pexels.com/photos/28930671/pexels-photo-28930671/free-photo-of-organic-peanut-trade-in-zaria-market.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="Agriculture is the foundation of civilization and any stable economy."
    Carousel_3p="-Allan Savory"
    Go_back=reverse('CAFENR_home')


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
        'Go_back': Go_back
    })
def BAE_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor in Agricultural Technology"
    css_style = "cafenr.css"
    College_Name = "College Of Agriculture, Forestry, Environment and Natural Resources"
    Carousel_1img ="https://images.pexels.com/photos/3912372/pexels-photo-3912372.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Innovation is the central issue in economic prosperity, and nowhere is this truer than in agriculture."
    Carousel_1p="-William Baumol"
    Carousel_2img="https://images.pexels.com/photos/2818573/pexels-photo-2818573.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Agricultural technology is a powerful tool that can improve efficiency, conserve resources, and enhance food security"
    Carousel_2p="-Norman Borlaug"
    Carousel_3img ="https://images.pexels.com/photos/27469249/pexels-photo-27469249/free-photo-of-a-small-drone-flying-over-a-field.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="Drones, AI, and automation will change the way we farm in ways we can only imagine."
    Carousel_3p="- Elon Musk"
    Go_back=reverse('CAFENR_home')


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
        'Go_back': Go_back
    })
def BSES_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science In Environmental Science"
    css_style = "cafenr.css"
    College_Name = "College Of Agriculture, Forestry, Environment and Natural Resources"
    Carousel_1img ="https://images.pexels.com/photos/1296265/pexels-photo-1296265.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="What we are doing to the forests of the world is but a mirror reflection of what we are doing to ourselves and to one another."
    Carousel_1p="- Mahatma Gandhi"
    Carousel_2img ="https://images.pexels.com/photos/1658967/pexels-photo-1658967.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="The environment is where we all meet; it is the one thing we all share."
    Carousel_2p="-Lady Bird Johnson"
    Carousel_3img ="https://images.pexels.com/photos/30574675/pexels-photo-30574675/free-photo-of-wind-turbine-against-blue-sky-in-bengaluru.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="Sustainability is no longer about doing less harm. It’s about doing more good."
    Carousel_3p="- Jochen Zeitz"
    Go_back=reverse('CAFENR_home')


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
        'Go_back': Go_back
    })
def BSFT_Quiz(request):
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science In Food Technology"
    css_style = "cafenr.css"
    College_Name = "College Of Agriculture, Forestry, Environment and Natural Resources"
    Carousel_1img ="https://images.pexels.com/photos/8940363/pexels-photo-8940363.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Technology is the future of food innovation, ensuring safety, efficiency, and nutrition."
    Carousel_1p="-George Santayana"
    Carousel_2img ="https://images.pexels.com/photos/6208936/pexels-photo-6208936.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Food science is the bridge between agriculture and nutrition, ensuring safe and sustainable consumption"
    Carousel_2p="-Harold McGee"
    Carousel_3img ="https://images.pexels.com/photos/2862154/pexels-photo-2862154.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="A well-balanced diet is the key to a healthy life, and food technology helps make that possible."
    Carousel_3p="- Michael Pollan"
    Go_back=reverse('CAFENR_home')


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
        'Go_back': Go_back
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
    College_Name = "College of Education"
    Carousel_1img ="https://images.pexels.com/photos/28136710/pexels-photo-28136710/free-photo-of-leadenhall.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Education is not the filling of a pail, but the lighting of a fire."
    Carousel_1p="-William Butler Yeats"
    Carousel_2img ="https://images.pexels.com/photos/20178392/pexels-photo-20178392/free-photo-of-directional-signs-by-thames-in-england.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="A word after a word after a word is power."
    Carousel_2p="-Margaret Atwood"
    Carousel_3img ="https://images.pexels.com/photos/5676740/pexels-photo-5676740.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="To learn to read is to light a fire; every syllable that is spelled out is a spark."
    Carousel_3p="-Victor Hugo"
    Go_back=reverse('CED_home')


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
        'Go_back': Go_back
    })
def BSE_FILI_Quiz(request):
    css_style = "ced.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Secondary Education Major In Filipino"
    College_Name = "College of Education"
    Carousel_1img ="https://images.pexels.com/photos/25785221/pexels-photo-25785221/free-photo-of-close-up-of-the-jose-rizal-monument-in-manila-philippines.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Ang hindi marunong magmahal sa sariling wika ay masahol pa sa hayop at malansang isda."
    Carousel_1p="-Jose Rizal"
    Carousel_2img ="https://images.pexels.com/photos/3698534/pexels-photo-3698534.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Ang wika ay kaluluwa ng isang bansa at salamin ng kultura at kasaysayan."
    Carousel_2p="-Lope K. Santos"
    Carousel_3img ="https://images.pexels.com/photos/2405644/pexels-photo-2405644.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="Ang wika ay may buhay, lumalago at yumayaman sa paggamit."
    Carousel_3p="- Virgilio Almario"
    Go_back=reverse('CED_home')


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
        'css_style' : css_style,
        'COURSE_NAME': COURSE_NAME,
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
        'Go_back': Go_back
    })
def BSE_MATH_Quiz(request):
    css_style = "ced.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Secondary Education Major In Math"
    College_Name = "College of Education"
    Carousel_1img ="https://images.pexels.com/photos/8472872/pexels-photo-8472872.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Mathematics is the language with which God has written the universe."
    Carousel_1p="-Galileo Galilei"
    Carousel_2img ="https://images.pexels.com/photos/4778670/pexels-photo-4778670.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Without mathematics, there’s nothing you can do. Everything around you is mathematics. Everything around you is numbers."
    Carousel_2p="-Shakuntala Devi"
    Carousel_3img ="https://images.pexels.com/photos/5147908/pexels-photo-5147908.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="Do not worry about your difficulties in mathematics; I assure you that mine are greater."
    Carousel_3p="-Albert Einstein"
    Go_back=reverse('CED_home')


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
        'css_style' : css_style,
        'COURSE_NAME': COURSE_NAME,
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
        'Go_back': Go_back
    })
def BSE_SCIE_Quiz(request):
    css_style = "ced.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Secondary Education Major In Science"
    College_Name = "College of Education"
    Carousel_1img ="https://images.pexels.com/photos/674318/pexels-photo-674318.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Science and everyday life cannot and should not be separated."
    Carousel_1p="-Rosalind Franklin"
    Carousel_2img ="https://images.pexels.com/photos/3645203/pexels-photo-3645203.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Somewhere, something incredible is waiting to be known."
    Carousel_2p="-Carl Sagan"
    Carousel_3img ="https://images.pexels.com/photos/30404439/pexels-photo-30404439/free-photo-of-rhesus-macaque-sitting-on-barrier-outdoors.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="The important thing is to never stop questioning. Curiosity has its own reason for existing."
    Carousel_3p="-Albert Einstein"
    Go_back=reverse('CED_home')

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
        'css_style' : css_style,
        'COURSE_NAME': COURSE_NAME,
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
        'Go_back': Go_back
    })
def BSE_SS_Quiz(request):
    css_style = "ced.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Secondary Education Major In Social Studies"
    College_Name = "College of Education"
    Carousel_1img ="https://images.pexels.com/photos/7507496/pexels-photo-7507496.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Those who do not remember the past are condemned to repeat it."
    Carousel_1p="-George Santayana"
    Carousel_2img ="https://images.pexels.com/photos/3747542/pexels-photo-3747542.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Education is the most powerful weapon which you can use to change the world."
    Carousel_2p="-Nelson Mandela"
    Carousel_3img ="https://images.pexels.com/photos/2346289/pexels-photo-2346289.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="A people without the knowledge of their past history, origin, and culture is like a tree without roots."
    Carousel_3p="- Marcus Garvey"
    Go_back=reverse('CED_home')

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
        'css_style' : css_style,
        'COURSE_NAME': COURSE_NAME,
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
        'Go_back': Go_back
    })

def BEED_Quiz(request):
    css_style = "ced.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Elementary Education"
    College_Name = "College of Education"
    Carousel_1img ="https://images.pexels.com/photos/1646953/pexels-photo-1646953.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Children must be taught how to think, not what to think"
    Carousel_1p="-Margaret Mead"
    Carousel_2img ="https://images.pexels.com/photos/3971983/pexels-photo-3971983.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Teaching kids to count is fine, but teaching them what counts is best."
    Carousel_2p="-Bob Talbert"
    Carousel_3img ="https://images.pexels.com/photos/6827516/pexels-photo-6827516.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="The art of teaching is the art of assisting discovery"
    Carousel_3p="-Mark Van Doren"
    Go_back=reverse('CED_home')

    if request.method == "POST":
        form = BEEDQuiz(request.POST)
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

            if answer_q3 == '1':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is A"    
    else:
        form = BEEDQuiz()

    return render(request, 'cvsuquiz/quiz.html', {
        'form': form, 
        'feedback_q1': feedback_q1,
        'feedback_q2': feedback_q2,
        'feedback_q3': feedback_q3,
        'css_style' : css_style,
        'COURSE_NAME': COURSE_NAME,
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
        'Go_back': Go_back
    })
def BSHM_Quiz(request):
    css_style = "ced.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Hotel and Restaurant Management "
    College_Name = "College of Education"
    Carousel_1img ="https://images.pexels.com/photos/4350205/pexels-photo-4350205.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Hospitality is simply an opportunity to show love and care"
    Carousel_1p="-Julia Sugarbaker"
    Carousel_2img ="https://images.pexels.com/photos/30427271/pexels-photo-30427271/free-photo-of-elegant-martini-glass-in-a-stylish-bar-setting.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="The key is to set realistic customer expectations and then not to just meet them, but to exceed them"
    Carousel_2p="-Richard Branson"
    Carousel_3img ="https://images.pexels.com/photos/8952192/pexels-photo-8952192.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="The best way to find yourself is to lose yourself in the service of others."
    Carousel_3p="-Mahatma Gandhi"
    Go_back=reverse('CED_home')

    if request.method == "POST":
        form = BSHMQuiz(request.POST)
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
        form = BSHMQuiz()

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
        'Go_back': Go_back
    })
def BSTM_Quiz(request):
    css_style = "ced.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in tourism Management"
    College_Name = "College of Education"
    Carousel_1img ="https://images.pexels.com/photos/3254753/pexels-photo-3254753.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Travel makes one modest. You see what a tiny place you occupy in the world."
    Carousel_1p="- Gustave Flaubert"
    Carousel_2img ="https://images.pexels.com/photos/20349049/pexels-photo-20349049/free-photo-of-boat-on-river-in-city.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="The world is a book, and those who do not travel read only one page."
    Carousel_2p="-Saint Augustine"
    Carousel_3img ="https://images.pexels.com/photos/586687/pexels-photo-586687.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="To travel is to discover that everyone is wrong about other countries."
    Carousel_3p="- Aldous Huxley"
    Go_back=reverse('CED_home')

    if request.method == "POST":
        form = BSTMQuiz(request.POST)
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
        form = BSTMQuiz()

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
        'Go_back': Go_back
    })


# ------  CCJ ---------
def ccj_home_view(request):
    return render(request, 'cvsuquiz/ccj.html')

def BSC_Quiz(request):
    COURSE_NAME = "Bachelor of Science in Criminology"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    css_style = "cspear.css"
    College_Name = "College of Criminal Justice"
    Carousel_1img ="https://images.pexels.com/photos/30617264/pexels-photo-30617264/free-photo-of-exciting-hockey-game-at-delta-center-arena.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Sport has the power to change the world. It has the power to inspire. It has the power to unite people in a way that little else does."
    Carousel_1p="-Nelson Mandela"
    Carousel_2img ="https://images.pexels.com/photos/159607/basketball-player-girls-basketball-girl-159607.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Sport is part of every man and woman’s heritage and its absence can never be compensated for."
    Carousel_2p="-Pierre de Coubertin"
    Carousel_3img ="https://images.pexels.com/photos/159515/football-american-football-runner-player-159515.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="The man who can drive himself further once the effort gets painful is the man who will win."
    Carousel_3p="-Roger Bannister"
    Go_back=reverse('CCJ_home')



    if request.method == "POST":
        form = BSCQuiz(request.POST)
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
        form = BSCQuiz()

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
        'Go_back': Go_back
    })

def BSISM_Quiz(request):
    COURSE_NAME = "Bachelor of Science in Industrial Security Management"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    css_style = "cspear.css"
    College_Name = "College of Criminal Justice"
    Carousel_1img ="https://images.pexels.com/photos/30617264/pexels-photo-30617264/free-photo-of-exciting-hockey-game-at-delta-center-arena.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Sport has the power to change the world. It has the power to inspire. It has the power to unite people in a way that little else does."
    Carousel_1p="-Nelson Mandela"
    Carousel_2img ="https://images.pexels.com/photos/159607/basketball-player-girls-basketball-girl-159607.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Sport is part of every man and woman’s heritage and its absence can never be compensated for."
    Carousel_2p="-Pierre de Coubertin"
    Carousel_3img ="https://images.pexels.com/photos/159515/football-american-football-runner-player-159515.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="The man who can drive himself further once the effort gets painful is the man who will win."
    Carousel_3p="-Roger Bannister"
    Go_back=reverse('CCJ_home')



    if request.method == "POST":
        form = BSCQuiz(request.POST)
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
        form = BSCQuiz()

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
        'Go_back': Go_back
    })
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
    Go_back=reverse('CAS_home')


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
        'Go_back': Go_back,
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
    Go_back=reverse('CAS_home')


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
        'Go_back': Go_back,
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
    Go_back=reverse('CAS_home')


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
        'Go_back': Go_back,
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
    Go_back=reverse('CAS_home')
    


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
        'Go_back': Go_back,
        
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
    Go_back=reverse('CAS_home')


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
        'Go_back': Go_back,
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
    Go_back=reverse('CAS_home')
    


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
        'Go_back': Go_back,
        
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
    Go_back=reverse('CAS_home')


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
        'Go_back': Go_back,
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
    Go_back=reverse('CAS_home')


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
        'Go_back': Go_back,
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
    Go_back=reverse('CAS_home')


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
        'Go_back': Go_back,
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
    Go_back=reverse('CAS_home')


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
        'Go_back': Go_back,
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
    Go_back=reverse('CAS_home')


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
        'Go_back': Go_back,
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
    Go_back=reverse('CON_home')


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
        'Go_back': Go_back,
    })

# ------  CON ---------
def con_home_view(request):
    return render(request, 'cvsuquiz/con.html')
def BSMT_QUIZ(request):
    css_style = "con.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Medical Technology"
    College_Name = "College of Nursing"
    Carousel_1img ="https://images.pexels.com/photos/8088861/pexels-photo-8088861.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="The greatest asset of a laboratory is not its equipment, but its people."
    Carousel_1p="-James Watson"
    Carousel_2img ="https://images.pexels.com/photos/3786154/pexels-photo-3786154.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Science moves with the spirit of an adventure characterized both by youthful arrogance and by the belief that the truth, once found, would be simple as well as pretty"
    Carousel_2p="-Paul Nurse"
    Carousel_3img ="https://images.pexels.com/photos/2280547/pexels-photo-2280547.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="If you know you are on the right track, if you have this inner knowledge, then nobody can turn you off... no matter what they say."
    Carousel_3p="-Barbara McClintock"
    Go_back=reverse('CON_home')


    if request.method == "POST":
        form = BSMT_Quiz(request.POST)
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
        form = BSMT_Quiz()

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
        'Go_back': Go_back,
    })
def BSM_QUIZ(request):
    css_style = "con.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Midwifery"
    College_Name = "College of Nursing"
    Carousel_1img ="https://images.pexels.com/photos/3259625/pexels-photo-3259625.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Good maternity care starts with respect."
    Carousel_1p="-Ina May Gaskin"
    Carousel_2img ="https://images.pexels.com/photos/2869318/pexels-photo-2869318.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="The best way to save the world is to birth and raise healthy, happy children."
    Carousel_2p="-Robin Lim"
    Carousel_3img ="https://images.pexels.com/photos/30044831/pexels-photo-30044831/free-photo-of-heartwarming-family-moment-with-newborn-baby.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="Birth isn’t something we suffer, but something we actively do and exult in."
    Carousel_3p="-Sheila Kitzinger"
    Go_back=reverse('CON_home')


    if request.method == "POST":
        form = BSM_Quiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '4':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is D"

            if answer_q2 == '1':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is A"

            if answer_q3 == '2':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is B"    
    else:
        form = BSM_Quiz()

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
        'Go_back': Go_back,
    })
def BSN_QUIZ(request):
    css_style = "con.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Nursing"
    College_Name = "College of Nursing"
    Carousel_1img ="https://images.pexels.com/photos/3845115/pexels-photo-3845115.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="For the sick, it is important to have the best."
    Carousel_1p="-Florence Nightingale"
    Carousel_2img ="https://images.pexels.com/photos/6129234/pexels-photo-6129234.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="The nurse is temporarily the consciousness of the unconscious, the love of life for the suicidal, the leg of the amputee, the eyes of the newly blind, a means of locomotion for the infant, knowledge and confidence for the young mother, the mouthpiece for those too weak or withdrawn to speak."
    Carousel_2p="-Virginia Henderson"
    Carousel_3img ="https://images.pexels.com/photos/5327865/pexels-photo-5327865.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="As a nurse, we have the opportunity to heal the heart, mind, soul, and body of our patients, their families, and ourselves."
    Carousel_3p="-Maya Angelou"
    Go_back=reverse('CON_home')


    if request.method == "POST":
        form = BSN_Quiz(request.POST)
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

            if answer_q3 == '1':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is A"    
    else:
        form = BSN_Quiz()

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
        'Go_back': Go_back,
    })
# ------  CEIT ---------
def ceit_home_view(request):
    return render(request, 'cvsuquiz/ceit.html')
def BSABE_QUIZ(request):
    css_style = "ceit.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science In Agricultural and Biosystems Engineering"
    College_Name = "College of Engineering and Information Technology"
    Carousel_1img ="https://images.pexels.com/photos/23698640/pexels-photo-23698640/free-photo-of-scenic-view-of-a-farm-with-a-wind-turbine-and-mountains-in-the-background.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="The best way to predict the future is to create it."
    Carousel_1p="-Peter Drucker"
    Carousel_2img ="https://images.pexels.com/photos/16692986/pexels-photo-16692986/free-photo-of-drone-in-rural-scenery.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Engineering is the art of directing the great sources of power in nature for the use and convenience of man."
    Carousel_2p="-Thomas Tredgold"
    Carousel_3img ="https://images.pexels.com/photos/16511757/pexels-photo-16511757/free-photo-of-rows-of-lush-lettuce-beds-in-a-greenhouse.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="The ultimate goal of farming is not the growing of crops, but the cultivation and perfection of human beings."
    Carousel_3p="-Masanobu Fukuoka"
    Go_back=reverse('CEIT_home')


    if request.method == "POST":
        form = BSABE_Quiz(request.POST)
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
        form = BSABE_Quiz()

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
        'Go_back': Go_back
    })
def BSARCH_QUIZ(request):
    css_style = "ceit.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science In Architecture"
    College_Name = "College of Engineering and Information Technology"
    Carousel_1img ="https://scontent.fcrk3-1.fna.fbcdn.net/v/t39.30808-6/475525317_4764273517131662_5888292757694974785_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=127cfc&_nc_ohc=AeiV0WpDHsMQ7kNvgEkPbBp&_nc_zt=23&_nc_ht=scontent.fcrk3-1.fna&_nc_gid=AUkmpavA2p9V4jw0aBBPeMb&oh=00_AYCJk4RD8eY3FhXVGNe0AloXJWKXAO4F_O0GQdo1uXu6kw&oe=67A01A89"
    Carousel_1h5="Architecture should speak of its time and place, but yearn for timelessness."
    Carousel_1p="-Frank Gehry"
    Carousel_2img ="https://scontent.fcrk3-4.fna.fbcdn.net/v/t39.30808-6/475307401_4764273557131658_5286387228374123926_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=127cfc&_nc_ohc=6m10DzeXN3EQ7kNvgFSMPuj&_nc_zt=23&_nc_ht=scontent.fcrk3-4.fna&_nc_gid=AfembqTUxXRi_JE_WbET7t2&oh=00_AYCynO1utBU3YWs-kn-5V1aqJMmqBAJm9p5S3U0xJd3-mQ&oe=67A00ED2"
    Carousel_2h5="Form follows function that has been misunderstood. Form and function should be one, joined in a spiritual union."
    Carousel_2p="-Frank Lloyd Wright"
    Carousel_3img ="https://scontent.fcrk3-4.fna.fbcdn.net/v/t39.30808-6/475533252_4764273533798327_4956764252380304385_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=127cfc&_nc_ohc=KJrv6CdDzIkQ7kNvgG2Rd4U&_nc_zt=23&_nc_ht=scontent.fcrk3-4.fna&_nc_gid=ApfARypAzixCz5TCl6RRmgQ&oh=00_AYDg7rei8fl05fUoR4OumhvVXfdv2SFHlk_URBcCDd3rVg&oe=67A028D4"
    Carousel_3h5="Architecture is the learned game, correct and magnificent, of forms assembled in light."
    Carousel_3p="-Le Corbusier"
    Go_back=reverse('CEIT_home')


    if request.method == "POST":
        form = BSARCH_Quiz(request.POST)
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
        form = BSARCH_Quiz()

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
        'Go_back': Go_back
    })
def BSCE_QUIZ(request):
    css_style = "ceit.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science In Civil Engineering"
    College_Name = "College of Engineering and Information Technology"
    Carousel_1img ="https://images.pexels.com/photos/258347/pexels-photo-258347.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="The chief function of the civil engineer is to provide and maintain the means by which human activity can be carried on and the civilization which we enjoy can be preserved."
    Carousel_1p="-Thomas Tredgold"
    Carousel_2img ="https://www.maccaferri.com/ph/wp-content/uploads/2023/01/09_TerraMesh-Wall-min-scaled-1.jpg"
    Carousel_2h5="Civil engineering is the art of making a living from the earth by building on it."
    Carousel_2p="-Henri Vidal"
    Carousel_3img ="https://images.pexels.com/photos/4976482/pexels-photo-4976482.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="A bridge is a work of art as much as it is a functional structure."
    Carousel_3p="-Othmar Ammann "
    Go_back=reverse('CEIT_home')


    if request.method == "POST":
        form = BSCE_Quiz(request.POST)
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
        form = BSCE_Quiz()

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
        'Go_back': Go_back
    })
def BSCpE_QUIZ(request):
    css_style = "ceit.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science In Computer Engineering"
    College_Name = "College of Engineering and Information Technology"
    Carousel_1img ="https://images.pexels.com/photos/9242280/pexels-photo-9242280.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="The best way to predict the future is to invent it."
    Carousel_1p="-Alan Kay"
    Carousel_2img ="https://images.pexels.com/photos/16062771/pexels-photo-16062771/free-photo-of-closeup-of-an-illuminated-electronic-equipment.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="The function of good software is to make the complex appear to be simple."
    Carousel_2p="-Grady Booch"
    Carousel_3img ="https://images.pexels.com/photos/6477211/pexels-photo-6477211.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="Everybody should learn to program a computer because it teaches you how to think."
    Carousel_3p="-Steve Jobs"
    Go_back=reverse('CEIT_home')


    if request.method == "POST":
        form = BSCpE_Quiz(request.POST)
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

            if answer_q3 == 'A':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is A"    
    else:
        form = BSCpE_Quiz()

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
        'Go_back': Go_back
    })
def BSCS_QUIZ(request):
    css_style = "ceit.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science In Computer Science"
    College_Name = "College of Engineering and Information Technology"
    Carousel_1img ="https://images.pexels.com/photos/3861959/pexels-photo-3861959.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="A language that doesn't affect the way you think about programming is not worth knowing."
    Carousel_1p="-Alan Perlis"
    Carousel_2img ="https://images.pexels.com/photos/12899188/pexels-photo-12899188.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Simplicity is a great virtue but it requires hard work to achieve it and education to appreciate it."
    Carousel_2p="-Edsger W. Dijkstra"
    Carousel_3img ="https://images.pexels.com/photos/16129705/pexels-photo-16129705/free-photo-of-man-sitting-at-desk-working-on-computers.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="We build our computers the way we build our cities—over time, without a plan, on top of ruins."
    Carousel_3p="-Ellen Ullman"
    Go_back=reverse('CEIT_home')


    if request.method == "POST":
        form = BSCS_Quiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '3':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is C"

            if answer_q2 == '4':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is D"

            if answer_q3 == '2':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is B"    
    else:
        form = BSCS_Quiz()

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
        'Go_back': Go_back
    })
def BSEE_QUIZ(request):
    css_style = "ceit.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science In Electrical Engineering"
    College_Name = "College of Engineering and Information Technology" 
    Carousel_1img ="https://scontent.fmnl3-3.fna.fbcdn.net/v/t39.30808-6/476161155_4767525406806473_5502112482453047697_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeGzDsIcU0KZ14mSRgbM_IsTbZ5CBG7qXBptnkIEbupcGjqtlz0AhvcwYRnjY8i4f6GoKCwUIHhIlAIoBV_PPOfF&_nc_ohc=4_Ud1CXn25QQ7kNvgHKnwse&_nc_zt=23&_nc_ht=scontent.fmnl3-3.fna&_nc_gid=AQNEkJ8PkvO-EiG69nMEfK6&oh=00_AYAavMjDhWt_7Jv7xL-WqZh0NUnZkj4AnSxZ4-DzIrCZAw&oe=67A51713"
    Carousel_1h5="If you want to find the secrets of the universe, think in terms of energy, frequency, and vibration."
    Carousel_1p="-Nikola Tesla"
    Carousel_2img ="https://scontent.fmnl3-3.fna.fbcdn.net/v/t39.30808-6/475956923_4767525413473139_1965786059146978733_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeFDwuXa1-Z-hTrd2Tlh4_66_9CTWdjlhc7_0JNZ2OWFzqcPJdiiYW8RHEHximethKgqDNGGA_ZN4LQJLvl3jl8H&_nc_ohc=dHMbNBVkTDkQ7kNvgEs9F_3&_nc_zt=23&_nc_ht=scontent.fmnl3-3.fna&_nc_gid=AAjCdiwX5ReeRAyhCQ4fZ15&oh=00_AYDNdW9kvjCFxwRKfkxS5nrcJHFD396voT4If3gEpR3fJg&oe=67A4FEE4"
    Carousel_2h5="Genius is one percent inspiration and ninety-nine percent perspiration."
    Carousel_2p="-Thomas Edison"
    Carousel_3img ="https://scontent.fmnl3-4.fna.fbcdn.net/v/t39.30808-6/476074393_4767525416806472_5585231107442572540_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeGZtim0UCTLJ6AggPsCsXmZeuSDi-pUVMJ65IOL6lRUwnt7IyC2uEBZF4QOp7cl_sP-xDm-LQI7wMJ0LCzYBsVS&_nc_ohc=_X_y5rGP2roQ7kNvgEj0pz5&_nc_zt=23&_nc_ht=scontent.fmnl3-4.fna&_nc_gid=Au6ueBLhL2A-wEuowawWKqY&oh=00_AYBVeQpNxgqophWeR0rErmknqG-nrlLCxdWtw7LCw2CMjw&oe=67A50DD8"
    Carousel_3h5="But still try, for who knows what is possible?"
    Carousel_3p="-Michael Faraday"
    Go_back=reverse('CEIT_home')


    if request.method == "POST":
        form = BSEE_Quiz(request.POST)
        if form.is_valid():
            answer_q1 = form.cleaned_data['answer_q1']
            answer_q2 = form.cleaned_data['answer_q2']
            answer_q3 = form.cleaned_data['answer_q3']

            if answer_q1 == '3':
                feedback_q1 = "Correct!"
            else:
                feedback_q1 = "Wrong! The correct answer is c"

            if answer_q2 == '2':
                feedback_q2 = "Correct!"
            else:
                feedback_q2 = "Wrong! The correct answer is B"

            if answer_q3 == '3':
                feedback_q3 = "Correct!"
            else:
                feedback_q3 = "Wrong! The correct answer is C"    
    else:
        form = BSEE_Quiz()

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
        'Go_back': Go_back
    })
def BSINDT_AT_QUIZ(request):
    css_style = "ceit.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Industrial Technology Major In Automotive Technology"
    College_Name = "College of Engineering and Information Technology" 
    Carousel_1img ="https://images.pexels.com/photos/3599175/pexels-photo-3599175.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Failure is simply the opportunity to begin again, this time more intelligently"
    Carousel_1p="-Henry Ford"
    Carousel_2img ="https://images.pexels.com/photos/2834653/pexels-photo-2834653.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="The client is not always right"
    Carousel_2p="-Enzo Ferrari"
    Carousel_3img ="https://images.pexels.com/photos/30458012/pexels-photo-30458012/free-photo-of-silver-porsche-carrera-s-in-germany-street.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1for"
    Carousel_3h5="Change is easy. Improvement is far more difficult."
    Carousel_3p="-Ferdinand Porsche"
    Go_back=reverse('CEIT_home')


    if request.method == "POST":
        form = BSINDT_AT_Quiz(request.POST)
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
        form = BSINDT_AT_Quiz()

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
        'Go_back': Go_back
    })
def BSINDT_ET_QUIZ(request):
    css_style = "ceit.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Industrial Technology Major In Electrical Technology"
    College_Name = "College of Engineering and Information Technology" 
    Carousel_1img ="https://images.pexels.com/photos/414943/pexels-photo-414943.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="We will make electricity so cheap that only the rich will burn candles."
    Carousel_1p="-Thomas Edison"
    Carousel_2img ="https://images.pexels.com/photos/9799700/pexels-photo-9799700.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Thoroughly conscious ignorance is the prelude to every real advance in science."
    Carousel_2p="-James Clerk Maxwell"
    Carousel_3img ="https://images.pexels.com/photos/5767595/pexels-photo-5767595.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="Nothing is too wonderful to be true, if it be consistent with the laws of nature."
    Carousel_3p="-Michael Faraday"
    Go_back=reverse('CEIT_home')


    if request.method == "POST":
        form = BSINDT_ET_Quiz(request.POST)
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
        form = BSINDT_ET_Quiz()

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
        'Go_back': Go_back
    })
def BSINDT_EX_QUIZ(request):
    css_style = "ceit.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Industrial Technology Major In Electronics Technology"
    College_Name = "College of Engineering and Information Technology" 
    Carousel_1img ="https://images.pexels.com/photos/27977986/pexels-photo-27977986/free-photo-of-close-up-of-a-computer-motherboard-with-cpu-fan-and-ram.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="Information is the resolution of uncertainty"
    Carousel_1p="-Claude Shannon"
    Carousel_2img ="https://images.pexels.com/photos/6477199/pexels-photo-6477199.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="The present is theirs; the future, for which I really worked, is mine."
    Carousel_2p="-Nikola Tesla"
    Carousel_3img ="https://images.pexels.com/photos/9242900/pexels-photo-9242900.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="Sometimes it is the people no one imagines anything of who do the things that no one can imagine"
    Carousel_3p="-Alan Turing"
    Go_back=reverse('CEIT_home')


    if request.method == "POST":
        form = BSINDT_EX_Quiz(request.POST)
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
        form = BSINDT_EX_Quiz()

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
        'Go_back': Go_back
    })
def BSIT_QUIZ(request):
    css_style = "ceit.css"
    feedback_q1 = None
    feedback_q2 = None
    feedback_q3 = None
    COURSE_NAME = "Bachelor of Science in Information Technology"
    College_Name = "College of Engineering and Information Technology" 
    Carousel_1img ="https://images.pexels.com/photos/16129728/pexels-photo-16129728/free-photo-of-man-coding-on-pc.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_1h5="The most dangerous phrase in the language is, 'We’ve always done it this way.'"
    Carousel_1p="-Grace Hopper"
    Carousel_2img ="https://images.pexels.com/photos/2102416/pexels-photo-2102416.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_2h5="Great things in business are never done by one person; they're done by a team of people."
    Carousel_2p="-Steve Jobs"
    Carousel_3img ="https://images.pexels.com/photos/7988086/pexels-photo-7988086.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    Carousel_3h5="Talk is cheap. Show me the code."
    Carousel_3p="-Linus Torvalds"
    Go_back=reverse('CEIT_home')


    if request.method == "POST":
        form = BSIT_Quiz(request.POST)
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
        form = BSIT_Quiz()

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
        'Go_back': Go_back
    })
def BSOA_QUIZ(request):
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

# ------  CEMDS ---------
def cemds_home_view(request):
    return render(request, 'cvsuquiz/cemds.html')