from django import forms
from .models import AnswerEasyCspear

class AnswerECForms(forms.Form):
    answer = forms.ModelChoiceField(queryset=AnswerEasyCspear.objects.none(), widget=forms.RadioSelect)

    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answer'].queryset = AnswerEasyCspear.objects.filter(question=question)