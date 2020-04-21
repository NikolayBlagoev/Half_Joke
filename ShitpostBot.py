from random import randrange
from time import sleep
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance

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

# Adds toptext and bottom text
def addText(img,topText="",bottomText="BOTTOMTEXT",magnify=1):
    draw = ImageDraw.Draw(img)
    fontSize = int(img.height / 10)*magnify
    font = ImageFont.truetype("impact.ttf", fontSize)
    x = (img.width / 2 - len(topText) * int(fontSize / 4))
    y = 5
    draw.text((x - 2, y + 2), topText, font=font, fill="black")
    draw.text((x + 2, y + 2), topText, font=font, fill="black")
    draw.text((x - 2, y - 2), topText, font=font, fill="black")
    draw.text((x + 2, y - 2), topText, font=font, fill="black")
    draw.text((x, y), topText, (255, 255, 255), font=font)
    lines=bottomText.count("\n")+1

    fontSize =int( (img.height / 10 )* magnify/lines)
    font = ImageFont.truetype("impact.ttf", fontSize)
    x = (img.width / 2 - len(bottomText) * int(fontSize / 4)/2)
    y = img.height - 100*magnify*lines
    draw.text((x - 2, y + 2), bottomText, font=font, fill="black")
    draw.text((x + 2, y + 2), bottomText, font=font, fill="black")
    draw.text((x - 2, y - 2), bottomText, font=font, fill="black")
    draw.text((x + 2, y - 2), bottomText, font=font, fill="black")
    draw.text((x, y), bottomText, (255, 255, 255), font=font)
    return img

# Combines template and source

path ='-'
img = Image.open(path+"-",'r')

img2 = Image.open(path+"-")
yRatio=1200/img2.height
xRatio=650/img2.width
ration=max(xRatio,yRatio)
img2=img2.resize((int(img2.width*ration), int(img2.height*ration)))

background = Image.new('RGBA', (img.width, img.height), (0, 255, 255, 255))
background.paste(img2, (int(-img2.width/2+300), int(-img2.height/2+700)))

background.paste(img, (0, 0), mask=img)

img=background
img=deepfry(img)
img.save(path+'sample-out.png')
img.show();
sleep(3)
img = Image.open(path+"-",'r')
img=addText(img,"", "",1)

img.save(path+'sample-out.png')
img.show();


