from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import qrcode as qr
from fpdf import FPDF
images=[]
name='Sagar'
event_name='Bukkake '
course='SagarSucksSocks '
path=os.path.abspath(r"C:\Users\senthil\Documents\GitHub\rig\venv\rig\rigapp\1.jpeg")

def PlaceText():
    img = Image.open(path)
    draw = ImageDraw.Draw(img)
    fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')
    print(fonts_path)
    font = ImageFont.truetype("arial.ttf", 56)
    draw.text((500, 500),"Name: %s"%name,(0,0,0),font=font)
    draw.text((500, 600),"Event Name: %s" %event_name ,(0,0,0),font=font)
    draw.text((500, 700),"Course: %s"%course,(0,0,0),font=font)
    img.save('xd.png')


def qrgen():
    #img=Image.open("xd.png")
    img=qr.make('SAGARLOVESCOCKS')
    img1=Image.open('xd.png')
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


pdf.output('xd2d.pdf')
