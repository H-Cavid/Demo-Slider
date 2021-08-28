from typing import ContextManager
from django.shortcuts import render
from .models import *
# Create your views here.
def HomeView(request):
    obj = Carausel.objects.all()
    context = {
        'obj' : obj,
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')