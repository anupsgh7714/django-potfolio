from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from projects.models import Projects

def home(request):
    return render(request,'home.html')

def projects(request):
    project_data = Projects.objects.all()
    data = {
        'project_data' : project_data 
    }
    return render(request,'projects.html',data)

def contact(request):
    return render(request,'contact.html')