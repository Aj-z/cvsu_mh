from django.shortcuts import render, redirect, get_object_or_404
from .models import QuestionsEasyCspear, AnswerEasyCspear
from .forms import AnswerECForms

# Create your views here.

def quiz_home(request):
    return render(request, 'quiz_home.html')

def question_view(request, question_id):
    question = get_object_or_404(QuestionsEasyCspear, id=question_id)
    
    if request.method == 'POST':
        form = AnswerECForms(question, request.POST)
        if form.is_valid():
            selected_answer = form.cleaned_data['answer']
            if selected_answer.is_correct:
                return render(request, 'correct.html', {'question': question})
            else:
                return render(request, 'incorrect.html', {'question': question})
    else:
        form = AnswerECForms(question)

    return render(request, 'question.html', {'question': question, 'form': form})