from .forms import StuForm, StuLoginForm
from .models import Students
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,JsonResponse
from rest_framework import compat
from django.views import View
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.views import APIView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json

# Show List of All Data
@login_required(login_url="/login/")
def home(request):
    query = request.GET.get("qury", None)
    obj = Students.objects.all().values()
    context = {"object_list" : obj}
    template = "allStuList.html"    
    return render(request, template, context)

# Create a New Student
@login_required(login_url="/login/")
def create(request):
    form = StuForm(request.POST,request.FILES)
    template = "createStu.html"
    context = {"form": form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/adminhome/")
    else: 
        form = StuForm()   
    return render(request, template, context)

# Get Infomation of Particular Student According to Id 
# @login_required(login_url="/login/")
def detail_view(request, id=None):
    qs = get_object_or_404(Students, id=id)
    context = {"object" : qs}
    template = "getStuData.html"
    return render(request, template, context) 

# Get Infomation of Particular Student According to Id 
# @login_required(login_url="/login/")
def studata(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        name = request.POST.get('name')        
        form = StuLoginForm(request.POST)
        qs = Students.objects.filter(name=name)
        if Students.objects.filter(name=name).exists():
            if (qs.filter(password=password).exists()):
                if form.is_valid():
                    obj = Students.objects.filter(name=name) 
                    context = {"object_list" : obj}
                    template = "stutem.html"   
                    # messages.success(request, 'Login successfully!') 
                    return render(request, template, context)
            else:
                messages.info(request, 'Enter the Correct Password!')
                return HttpResponseRedirect("/studentlogin/")
        else:
            messages.info(request, 'Enter the Correct Name!')
            return HttpResponseRedirect("/studentlogin/") 
    else: 
        form = StuLoginForm()   
    return render(request, "stulogin.html", {"form": form})

def stulogout(request):
    return HttpResponseRedirect("/studentlogin/")
 