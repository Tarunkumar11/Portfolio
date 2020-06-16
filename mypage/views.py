from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.http import HttpResponse
from mypage.forms import ContactForm
from django.views.generic import (TemplateView)
from mypage.models import Contact,resume
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core.files import File
from django.views.generic import (TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView,
                                    RedirectView)
from django.template import loader
from django.template import Context

def index(request):
    return render(request,'mypage/index.html')
def project(request):
    return render(request,'mypage/project.html')
def resume(request):
    return render(request,'mypage/resume.html')


def CreateContact(request):
    if request.method == "POST":
        if  request.POST.get('Name')  and request.POST.get('email')  and request.POST.get('message'):
            mold = Contact()
            mold.Name = request.POST.get('Name')
            mold.email = request.POST.get('email')
            mold.message = request.POST.get('message')
            mold.save()
            messages.success(request,"Message has been received")
            print("sucessuew")
            #return render(request,'mypage/index.html')
        else:
            print("Nooooooooooo")
            messages.error(request, 'Please Fill the information correctly')
            
    return render(request,'mypage/index.html')


def download(request):
    return render(request, 'mypage/index.html', Context({'Resume':resume.objects.first()}))






"""def download_file(request):
    # fill these variables with real values
    fl_path = '/media/here.jpg'
    filename = 'downloaded_file_name.extension'
    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response"""


#    my_help = {'help_me':'i am tarun saini and i need your help to solve this'}
#    return render(request,'first_app/help.html',context= my_help)

#def home_page(request):
#    return render(request,'first_app/home_page.html')
