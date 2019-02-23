from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^feedbacktypes/', include('feedbacktypes.urls')),
]

urlpatterns += staticfiles_urlpatterns()
