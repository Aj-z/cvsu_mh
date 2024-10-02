from django import forms
from .models import AnswerEasyCspear

class QuizForm(forms.Form):
    CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ]
    
    answer = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect,
        label="What is 1 + 1?"
    )