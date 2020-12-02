import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        #@@@@@@@@@@@@@@@@@@@@@@@ el dia de hoy menos un dia ( o sea ayer)
        #Seria> si la publicacion es de ayer o mayor hasta hace unos
        #segundos entoneces es TRUE (reciente)
        
class Choice(models.Model):
    #Que a cada Choice le corresponde una question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

