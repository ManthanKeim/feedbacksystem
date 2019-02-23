from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

app_name='feedback'

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name = "logout"),
]