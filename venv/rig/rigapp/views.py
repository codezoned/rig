from django.shortcuts import render
from django.http import HttpResponse

def hellopage(request):
    return HttpResponse("<h2>Hello World!!</h2>")

# Create your views here.
