from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import os
import sys
path=os.path.abspath(r"path to id.py")


def index(request):
    if request.method =='GET':
        return render(request,'home.html')
    elif request.method =='POST':
        submit(request)

        return render(request,'home.html')


def submit(request):
    a=request.POST['a']
    b=request.POST['b']
    print("what the f")
    subprocess.call([sys.executable,path, a,b], cwd=r"path to working directory = rigapp")
