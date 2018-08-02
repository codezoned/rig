from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import os
import sys
path=os.path.abspath(r"C:\Users\senthil\Documents\GitHub\rig\venv\rig\rigapp\id.py")


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
    subprocess.call([sys.executable,path, a], cwd=r"C:\Users\senthil\Documents\GitHub\rig\venv\rig\rigapp")
