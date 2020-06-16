from django.conf.urls import url
from mypage import views
from . import forms
urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    url(r'projects/',views.project,name = 'projectpage'),
    url(r'Resume/',views.resume,name = 'resume'),
    url(r'^message', views.CreateContact, name= 'message'),
    url(r'^$', views.download, name= 'download_cv'),

    #url(r'^contact/',views.CreateContact,name = 'contact_here'),

]
