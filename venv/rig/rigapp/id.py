<<<<<<< HEAD
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import shutil

import qrcode as qr
import sys
from fpdf import FPDF
images=[]
name=sys.argv[1]
event_name=sys.argv[2]
course=sys.argv[2]
path=os.path.abspath(r"F:\New folder\codezoned\rig\venv\rig\rigapp\img.png")

def PlaceText():
    img = Image.open(path)
    draw = ImageDraw.Draw(img)
    fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')
    print(fonts_path)
    font = ImageFont.truetype("arial.ttf", 56)
    draw.text((500, 500),"Name: %s"%name,(0,0,0),font=font)
    draw.text((500, 600),"Event Name: %s" %event_name ,(0,0,0),font=font)
    draw.text((500, 700),"Course: %s"%course,(0,0,0),font=font)
    img.save('img.png')


def qrgen():
    #img=Image.open("xd.png")
    img=qr.make(name)
    img1=Image.open('img.png')
    img1.paste(img)
    img1.save('qr.png')

PlaceText()
qrgen()
pdf=FPDF()
image='qr.png'
pdf.add_page()
pdf.image(image,x=0,y=0,w=100,h=100)
pdf.image(image,x=110,y=0,w=100,h=100)
pdf.image(image,x=110,y=110,w=100,h=100)
pdf.image(image,x=0,y=110,w=100,h=100)
os.remove("img.png")
shutil.copyfile('qr.png', './static/qr.png')  

pdf.output('Badge.pdf')
=======
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import shutil

import qrcode as qr
import sys
from fpdf import FPDF
images=[]
name=sys.argv[1]
event_name=sys.argv[2]
course=sys.argv[2]
path=os.path.abspath(r"F:\New folder\codezoned\rig\venv\rig\rigapp\img.png")

def PlaceText():
    img = Image.open(path)
    draw = ImageDraw.Draw(img)
    fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')
    print(fonts_path)
    font = ImageFont.truetype("arial.ttf", 56)
    draw.text((500, 500),"Name: %s"%name,(0,0,0),font=font)
    draw.text((500, 600),"Event Name: %s" %event_name ,(0,0,0),font=font)
    draw.text((500, 700),"Course: %s"%course,(0,0,0),font=font)
    img.save('img.png')


def qrgen():
    #img=Image.open("xd.png")
    img=qr.make(name)
    img1=Image.open('img.png')
    img1.paste(img)
    img1.save('qr.png')

PlaceText()
qrgen()
pdf=FPDF()
image='qr.png'
pdf.add_page()
pdf.image(image,x=0,y=0,w=100,h=100)
pdf.image(image,x=110,y=0,w=100,h=100)
pdf.image(image,x=110,y=110,w=100,h=100)
pdf.image(image,x=0,y=110,w=100,h=100)
os.remove("img.png")
shutil.copyfile('qr.png', './static/qr.png')  

pdf.output('Badge.pdf')
>>>>>>> 3fc839982a46b795fbc5828300776090fecca9bd
