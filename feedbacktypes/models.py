from django.db import models
import datetime
# Create your models here.
class FeedbackType(models.Model):
     title = models.CharField(max_length=100)
     slug = models.SlugField()
     body = models.TextField()

def __str__(self):
     return self.title

TEACHERS_NAMES = (
          ('Prof. R.K. Singh','STRM'),
          ('Dr. Arun Sharma','BD'),
          ('Ms. Charu Gupta','SCSE'),
          ('Mr. Rishabh Kausal','ADS'),
          ('Dr. Mohona Ghosh','CPA'),
          ('Mr. Gaurav Indra','CN'),
          ('Dr. Sourabh Bharti','TP'),
     )

class Teacher(models.Model):
     teacher_name = models.CharField(max_length=100, choices = TEACHERS_NAMES, default='---------')

class Question(models.Model):      
     question_text = models.CharField(max_length=200)
     pub_date = models.DateTimeField('date published')
    
def __str__(self):
    return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)

def __str__(self):
    return self.choice_text
