from django.db import models

# Create your models here.

### Cspear Easy Question model
class QuestionsEasyCspear (models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class AnswerEasyCspear(models.Model): 
    question = models.ForeignKey(QuestionsEasyCspear, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)    

    def __str__(self):
        return f'{self.text} ({self.is_correct})'