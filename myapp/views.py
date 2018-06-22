from django.shortcuts import render ,HttpResponse
from .models import Person
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



def home(request):
     return render(request,'myapp/index.html')

def profiles(request):
    p= Person.objects.filter()
    return render(request, 'myapp/profiles.html',{'p':p})
def getdetails(request):
    p = Person.objects.all()
    return render(request,"myapp/getdetails.html",{'p':p})
def index(request):
    return render(request,"myapp/index.html")

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return HttpResponse('myapp/profiles.html')
    else:
        form = AuthenticationForm()
        return render(request, 'myapp/login.html', {'form': form})





def logout_view(request):
    return render(request,"myapp/logout.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/myapp/profiles/")
    else:
        form= UserCreationForm()
        args= {'form': form}
        return render(request, 'myapp/reg_form.html', args)














