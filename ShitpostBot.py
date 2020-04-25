from random import randrange
from time import sleep
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance
import math
import os.path
import tweepy
path =''

api = tweepy.API(auth)

class Meme:
    def __init__(self, path, xEmptyArea,yEmptyArea, rotEmptyArea,xFocus,yFocus, hEmpty, wEmpty, text=""):
        self.path=path
        self.xEmptyArea=xEmptyArea
        self.yEmptyArea=yEmptyArea
        self.rotEmptyArea = rotEmptyArea
        self.xFocus=xFocus
        self.yFocus=yFocus
        self.hEmpty=hEmpty
        self.wEmpty=wEmpty
        self.text=text

class TextAddition:
    def __init__(self, topText, bottomText):
        self.topText=topText
        self.bottomText=bottomText

def fillWithSources():
    data=[]

    img2 = Meme("Random/Linus.png", 0, 0, 0, 315, 227, 0, 0)
    data.append(img2)
    return data
def fillWithTexts():
    data=[]

    txt = TextAddition("OK GOOGLE", "UNSHIT MY PANTS")
    data.append(txt)

    return data

def fillWithTemplates():
    data=[]

    img1 = Meme("Templates/EducationOpensALotOfDoors.png", 540, 752, 0, 0, 0, 532, 272)
    data.append(img1)

    return data
def fillOntTop():
    data=[]
    return data
# Completely ruins an image
def deepfry(img: Image):
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

def pasteOnTop(background,source):
    img1 = Image.open(path + background.path,'r')           # Background image
    img2 = Image.open(path + source.path, 'r')              # Source image
    yRatio = background.hEmpty / img2.height
    xRatio=background.wEmpty / img2.width
    ratio = min(xRatio, yRatio)
    img2 = img2.resize((int(img2.width * ratio), int(img2.height * ratio)))
    img1.paste(img2,(int(background.xEmptyArea-(img2.width/2)),int(background.yEmptyArea-(img2.height/2))))
    return img1

def pasteInside(template,source):
    img1 = Image.open(path + template.path, 'r')  # Template image
    img2 = Image.open(path + source.path, 'r')  # Source image
    background = Image.new("RGB", (img1.width, img1.height), "white")
    himg2=2*(min(source.yFocus, img2.height-source.yFocus))
    wimg2=2*(min(source.xFocus, img2.width-source.xFocus))
    yRatio = template.hEmpty / himg2
    xRatio=template.wEmpty / wimg2
    if yRatio>1 or xRatio>1:
        ratio = max(xRatio, yRatio)
    else:
        ratio = max(xRatio, yRatio)
    print(ratio)
    img2 = img2.resize((int(img2.width * ratio), int(img2.height * ratio)))
    background.paste(img2, (int(template.xEmptyArea - source.xFocus*ratio), int(template.yEmptyArea - source.yFocus*ratio)))
    background.paste(img1,(0,0),img1)
    return background


source= fillWithSources()
templates=fillWithTemplates()
putOnTop=fillOntTop()
texts=fillWithTexts()




for i in range(0,100):

    c=randrange(100)
    print(c)
    fileOutputName="1"
    cakdka=1
    outputText=""
    while os.path.isfile(path+"Product/"+fileOutputName+".png"):
        print('About to be in here:')
        print(cakdka)
        if c in range (0,11):
            img=source[randrange(len(source))-1]
            add = texts[randrange(len(texts))-1]
            img1 = Image.open(path + img.path, 'r')
            output=addText(img1,add.topText,add.bottomText)
            d = randrange(5)
            if d <2:
                output=deepfry(output)
            fileOutputName=str(hash(img.path))+"T"+str(hash(add.bottomText))
            outputText=img.text


        elif c in range (10,46):
            img=source[randrange(len(source))-1]
            img2= putOnTop[randrange(len(putOnTop))-1]
            output=pasteOnTop(img2,img)
            d = randrange(5)
            if d <2:
                output=deepfry(output)

            fileOutputName = str(hash(img.path))+"s"+ str(hash(img2.path))
            outputText = img2.text

        elif c in range(45, 101):
            img=source[randrange(len(source))-1]
            img2= templates[randrange(len(templates))-1]
            output=pasteInside(img2,img)
            d = randrange(5)
            if d <2:
                output=deepfry(output)

            fileOutputName = str(hash(img.path))+"s"+ str(hash(img2.path))
            outputText = img2.text

        cakdka+=1
    output.save(path + 'Product/' + fileOutputName + '.png')
    api.update_with_media(path + 'Product/' + fileOutputName + '.png', status=outputText)
    i = i + 1
    sleep(300)