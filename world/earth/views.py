from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("this is my home page")

def about(request):
        return HttpResponse("SEXY ABOUT")