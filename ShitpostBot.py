from random import randrange
from time import sleep
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance
import math
# Completely ruins an image
def deepfry(img):
    img = img.filter(ImageFilter.SHARPEN)
    img = img.filter(ImageFilter.SHARPEN)
    img = img.filter(ImageFilter.SHARPEN)
    img = ImageEnhance.Brightness(img).enhance(2)
    img = ImageEnhance.Color(img).enhance(2)
    img = ImageEnhance.Contrast(img).enhance(2)
    img = img.filter(ImageFilter.SHARPEN)
    img = img.filter(ImageFilter.SHARPEN)
    img = img.filter(ImageFilter.SHARPEN)
    img = img.filter(ImageFilter.SHARPEN)
    return img
def splitString(input):
    input=input.replace("\n"," ")
    output=[]
    const=30*max(1,int(len(input)/180))
    start=0
    end=const
    while end<len(input):
        if (input[end]!=" " or input[end]!="\n" or input[end]!="\0") :
            i=end
            p=end
            steps=0
            while steps<10:
                if i<len(input)and (input[i]==" " or input[i]=="\n" or input[i]=="\0"):
                    end=i
                    break
                if p>=0 and ( input[p] == " " or input[p] == "\n" or input[p] == "\0"):
                    end = p
                    break
                steps+=1
                i+=1
                p-=1

        output.append(input[start:end])
        start=end
        end+=const
    if start<len(input):
        output.append(input[start:])
    return output
def drawTextLowerBorder(draw,img, text,bottomy,magnify=1):
    text = splitString(text)
    lines = len(text)
    fontSize = int((img.height / 10) * magnify / max(math.ceil(lines / 2)-1,1))
    for i in range(len(text)):
        txt = text[i]
        font = ImageFont.truetype("impact.ttf", fontSize)
        (w, h) = draw.textsize(txt, font=font)
        x = int((img.width - w) / 2)
        y = bottomy - ( (len(text) - i) * h)
        draw.text((x - 2, y + 2), txt, font=font, fill="black")
        draw.text((x + 2, y + 2), txt, font=font, fill="black")
        draw.text((x - 2, y - 2), txt, font=font, fill="black")
        draw.text((x + 2, y - 2), txt, font=font, fill="black")
        draw.text((x, y), txt, (255, 255, 255), font=font)
def drawTextUpperBorder(draw,img, text,top,magnify=1):
    text = splitString(text)
    lines = len(text)
    fontSize = int((img.height / 10) * magnify / max(math.ceil(lines / 2)-1,1))
    for i in range(len(text)):
        txt = text[i]
        font = ImageFont.truetype("impact.ttf", fontSize)
        (w, h) = draw.textsize(txt, font=font)
        x = int((img.width - w) / 2)
        y = top + (i * h)
        draw.text((x - 2, y + 2), txt, font=font, fill="black")
        draw.text((x + 2, y + 2), txt, font=font, fill="black")
        draw.text((x - 2, y - 2), txt, font=font, fill="black")
        draw.text((x + 2, y - 2), txt, font=font, fill="black")
        draw.text((x, y), txt, (255, 255, 255), font=font)

# Adds toptext and bottom text
def addText(img,topText="",bottomText="BOTTOMTEXT",magnify=1):
    draw = ImageDraw.Draw(img)
    drawTextUpperBorder(draw,img,topText,5)
    drawTextLowerBorder(draw,img,bottomText,img.height-10)
    return img

# Combines template and source

path =''
img = Image.open(path+"",'r')
img=addText(img,"")

img.save(path+'sample-out.png')
img.show();


