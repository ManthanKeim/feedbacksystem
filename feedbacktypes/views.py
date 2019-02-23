from django.shortcuts import render
from .models import FeedbackType, Question, Choice, Teacher
from django.http import HttpResponse

# Create your views here.
def feedback_type(request):
    feedbacks = FeedbackType.objects.all()
    return render(request, 'feedbacktypes/feedback_type.html', {'feedbacks': feedbacks})

def feedback_type_detail(request):
    teachers = Teacher.objects.all()
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    #feedback_type = FeedbackType.objects.get(slug=slug)
    return render(request, 'feedbacktypes/teacher_feedback.html', {'latest_questions':latest_questions, 'teacher_name':teachers})
    #return HttpResponse(slug)
