from django.conf.urls import url
from . import views

app_name = 'feedbacktypes'

urlpatterns = [
    url(r'^$', views.feedback_type, name="list"),
    #named capturing group
    url(r'^form/', views.feedback_type_detail, name="detail"),
    #url(r'^(?P<slug>[\w-]+)/$', views.feedback_type_detail, name="detail"),
]
