from django.contrib import admin
from .models import FeedbackType, Question, Choice, Teacher

admin.site.register(FeedbackType)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Teacher)
