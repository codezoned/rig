from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import os
import sys
path=os.path.abspath(r"path to id.py")
fpath=os.path.abspath(r".\Badge.pdf")

def index(request):
    if request.method =='GET':
        return render(request,'home.html')
    elif request.method =='POST':
        submit(request)
        with open(fpath, 'rb') as pdf:
	           response = HttpResponse(pdf.read())
	           response['content_type'] = 'application/pdf'
	           response['Content-Disposition'] = 'attachment;filename=Badge.pdf'
	           return response
        #return render(request,'download.html')




def submit(request):
    a=request.POST['a']
    b=request.POST['b']
    print("Badge")
    subprocess.call([sys.executable,path, a,b], cwd=r"path to cwd")
