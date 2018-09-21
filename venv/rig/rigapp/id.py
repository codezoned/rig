
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import shutil
import pandas as pd
import qrcode
import time

import textwrap
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

import sys
from fpdf import FPDF
import time

user_font=sys.argv[1]+".ttf"
user_size=int(sys.argv[2])






start_time=time.time()





i=0
print(os.getcwd())

badge=pd.read_csv('data.csv')
col=badge.columns.values

picname=str(i)+'.png'

i=0
def PlaceText():
    name=badge[col[0]][i]
    tname=badge[col[1]][i]
    img = Image.open('upload.png')
    W , H =img.size

    draw = ImageDraw.Draw(img)
    fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')
    print(name)
    font = ImageFont.truetype(user_font, user_size)

    w, h = draw.textsize(name,font=font)
    #print((W-w)/2)
    offset=130
    draw.text(((W-w)/2,(H-h)/2-offset), name,  font=font, fill="white")
    w, h = draw.textsize(tname,font=font)
    draw.text(((W-w)/2,(H-h)/2-offset+100), tname,  font=font, fill="white")


    img.save(picname)


def qrgen():
    #img=Image.open("xd.png")
    qr.add_data(name)
    qr.make(fit=True)
    img=qr.make_image(fill_color="white", back_color="gray")
    img1=Image.open(picname)
    img1.paste(img)
    img1.save(picname)

k=0




pdf=FPDF()

def four():
    global i
    print (i)
    while(i<badge.index.size):
        pdf.add_page()
        picname=str(k)+'.png'
        PlaceText()
        #qrgen()
        image=picname
        pdf.image(image,x=10,y=10,w=90,h=120)
        i+=1
        if(i==badge.index.size):
            break




        picname=str(i)+'.png'
        print("1 over")


        picname=str(k)+'.png'
        PlaceText()
        #qrgen()
        image=picname
        pdf.image(image,x=110,y=10,w=90,h=120)
        i+=1

        if(i==badge.index.size):
            break




        picname=str(i)+'.png'




        picname=str(k)+'.png'
        PlaceText()
        #qrgen()
        image=picname
        pdf.image(image,x=10,y=140,w=90,h=120)
        i+=1

        if(i==badge.index.size):
            break




        picname=str(i)+'.png'



        picname=str(k)+'.png'
        PlaceText()
        #qrgen()
        image=picname
        pdf.image(image,x=110,y=140,w=90,h=120)
        i+=1

        if(i==badge.index.size):
            break


        picname=str(i)+'.png'


def one():
    global i
    print(i)

    while(i<badge.index.size):
        pdf.add_page()
        picname=str(i)+'.png'
        PlaceText()
        image=picname
        pdf.image(image,w=90,h=120)
        i=i+1
        if(i==badge.index.size):
            break
        picname=str(i)+'.png'
        #pdf.output('Badge.pdf')


#one()
four()

print("--- %s seconds ---" % (time.time() - start_time))
pdf.output('Badge.pdf')
os.remove("data.csv")
os.remove("upload.png")
