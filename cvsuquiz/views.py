from django.shortcuts import render
from .forms import QuizForm

def quiz_home_view(request):
    return render(request, 'cvsuquiz/quiz_home.html')

def quiz_home(request):
    feedback = None
    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            if answer == '2':
                feedback = "Correct!"
            else:
                feedback = "Wrong! The correct answer is 2."
    else:
        form = QuizForm()

    return render(request, 'cvsuquiz/cspear.html', {'form': form, 'feedback': feedback})