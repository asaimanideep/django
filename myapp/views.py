from django.shortcuts import render ,HttpResponse
from .models import Person
# Create your views here#
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
def home(request):
    return render(request,'myapp/index.html')

def profiles(request):
    p= Person.objects.all()
    #args={'p':p}
    return render(request, 'myapp/profiles.html',{'p':p})
def getdetails(request):
    p = Person.objects.all()
    return render(request,"myapp/getdetails.html",{'p':p})
def index(request):
    return render(request,"myapp/index.html")

