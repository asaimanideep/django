from django.shortcuts import render ,HttpResponse
from .models import Person
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
#from .forms import LoginForm
from django.contrib.auth.decorators import login_required



def home(request):
     return render(request,'myapp/index.html')

def getdetails(request):
    p = Person.objects.all()
    return render(request,"myapp/getdetails.html",{'p':p})
def index(request):
    return render(request,"myapp/index.html")

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user=form.get_user()
#             login(request, user)
#         return HttpResponse('myapp/profiles.html')
#     else:
#         form = AuthenticationForm()
#         return render(request, 'myapp/login.html', {'form': form})





def logout_view(request):
    return render(request,"myapp/logout.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
        return redirect("/myapp/profiles/")
    else:
        form= UserCreationForm()
        args= {'form': form}
        return render(request, 'myapp/reg_form.html', args)

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated '\
#                         'successfully')
#                 else:
#                         return HttpResponse('Disabled account')
#         else:
#             return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#         return render(request, 'myapp/login.html', {'form': form})
#
#





def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user=form.get_user()
            login(request,user)
            if'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('myapp:profiles')
            return redirect('myapp:profiles')

    else:
        form=AuthenticationForm()
    return render(request,'myapp/login.html',{'form':form})

@login_required(login_url="/myapp/login/")
def profiles(request):
    p= Person.objects.filter()
    return render(request, 'myapp/profiles.html',{'p':p})





