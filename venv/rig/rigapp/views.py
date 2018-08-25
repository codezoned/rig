from django.shortcuts import render
from django.http import HttpResponse
#from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage

import subprocess
import os
import sys
path=os.path.abspath(r"F:\New folder\codezoned\rig\venv\rig\rigapp\id.py")
fpath=os.path.abspath(r"F:\New folder\codezoned\rig\venv\rig\rigapp\Badge.pdf")
from django.core.files.storage import FileSystemStorage

def index(request):
    if request.method =='GET':
        return render(request,'rig2.html')
    #elif request.method =='POST':
    #    response=submit(request)
    #    return response
        #return render(request,'download.html')





def submit(request):
    a=request.POST['fname']
    b=request.POST['lname']
    folder=os.path.abspath(r"F:\New folder\codezoned\rig\venv\rig\rigapp")
    if(request.FILES):
        myf = request.FILES['pic']
        fs = FileSystemStorage(location=folder)
        filename = fs.save('img.png', myf)
    subprocess.call([sys.executable,path, a,b], cwd=r"F:\New folder\codezoned\rig\venv\rig\rigapp")
    return render(request,'download.html')


def down(request):
    print("does this work")
    with open(fpath, 'rb') as pdf:
           response = HttpResponse(pdf.read())
           response['content_type'] = 'application/pdf'
           response['Content-Disposition'] = 'attachment;filename=Badge.pdf'
           return response



def upload(request):
    print("IS THIS WORKING")
    folder=os.path.abspath(r"F:\New folder\codezoned\rig\venv\rig\rigapp" )
    if request.method == 'POST':
       myf = request.FILES['myfile']
       fs = FileSystemStorage(location=folder)
       filename = fs.save('img.png', myf)
