from django.shortcuts import render
from django.http import HttpResponse
#from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage

import subprocess
import os
import sys
from .models import Badge
cwd = os.getcwd()
path=cwd+"\\rigapp\id.py"
#path=os.path.abspath(r"F:\New folder\mine\rig\venv\rig\rigapp\id.py")
#fpath=os.path.abspath(r"F:\New folder\mine\rig\venv\rig\rigapp\Badge.pdf")
fpath=cwd+"\\rigapp\Badge.pdf"
cwd=cwd+"\\rigapp"
from django.core.files.storage import FileSystemStorage

def index(request):
    if request.method =='GET':
        return render(request,'rig2.html')
    #elif request.method =='POST':
    #    response=submit(request)
    #    return response
        #return render(request,'download.html')





def submit(request):
    a=request.POST['font']
    b=request.POST['size']
    folder=cwd
    if(request.FILES):
        myf = request.FILES['pic']
        fs = FileSystemStorage(location=folder)
        filename = fs.save('upload.png', myf)
        myf2=request.FILES['csv_file']
        fs = FileSystemStorage(location=folder)
        filename = fs.save('data.csv', myf2)

    subprocess.call([sys.executable,path, a,b], cwd=cwd)
    return render(request,'download.html')


def down(request):
    print("does this work")
    with open(fpath, 'rb') as pdf:
           response = HttpResponse(pdf.read())
           response['content_type'] = 'application/pdf'
           response['Content-Disposition'] = 'attachment;filename=Badge.pdf'
           return response
