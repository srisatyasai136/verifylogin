from django.shortcuts import render
from .forms import Loginform
from django.http import HttpResponse

import random
import string
import io


# with a white background with letters and strick mark line verify captcha image
# def captcha_image(request):
#     code=''.join(random.choices(string.ascii_uppercase+string.digits,k=5))
#     request.session['captcha']=code
#     image=Image.new('RGB',(150,50),color='white')
#     draw=ImageDraw.Draw(image)
#     draw.text((35,10),code,fill='black')
#     draw.line(((0,0),(150,50)),fill='blue')
#     draw.line(((0,100),(150,50)),fill='red')
#     buffer=io.BytesIO()
#     image.save(buffer,'PNG')
#     return HttpResponse(buffer.getvalue(),content_type='image/png')


import random,string,io
from django.http import HttpResponse
from PIL import Image,ImageDraw,ImageFont

def captcha_image(request):
    code=''.join(random.choices(string.ascii_uppercase+string.digits,k=4))
    request.session['captcha']=code

    width,height=150,50
    image=Image.new('RGB',(width,height),(255,255,255))
    draw=ImageDraw.Draw(image)

    for i in range(400):
        x=random.randint(0,width)
        y=random.randint(0,height)
        color=(random.randint(100,255),random.randint(100,255),random.randint(100,255))
        draw.point((x,y),fill=color)

    for i in range(5):
        x1=random.randint(0,width)
        y1=random.randint(0,height)
        x2=random.randint(0,width)
        y2=random.randint(0,height)

        draw.line(
            ((x1,y1),(x2,y2)),
            fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
            width=2
        )

    try:
    font=ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        30
    )
    except:
    font=ImageFont.load_default()

    x_position=10

    for char in code:
        char_img=Image.new('RGBA',(35,35),(255,255,255,0))
        char_draw=ImageDraw.Draw(char_img)

        color=(random.randint(0,150),random.randint(0,150),random.randint(0,150))

        char_draw.text((5,5),char,font=font,fill=color)

        angle=random.randint(-35,35)

        rotated=char_img.rotate(angle,expand=True)

        y=random.randint(5,15)

        image.paste(rotated,(x_position,y),rotated)

        x_position+=30

    buffer=io.BytesIO()
    image.save(buffer,format='PNG')

    return HttpResponse(buffer.getvalue(),content_type='image/png')

# Create your views here.
def signin(request):
    form=Loginform()
    error=None
    if request.method=="POST":
        form=Loginform(request.POST)
        if form.is_valid():
            entered=form.cleaned_data['captcha']
            actual=request.session.get('captcha')
            if entered==actual:
                return render(request,'home.html')
            error="Wrong verification code"
            data=request.POST.copy()
            data['captcha']=''
            form=Loginform(data)
            form.fields['password'].widget.attrs['value']=request.POST.get('password')
    return render(request,'login.html',{"form":form,"error":error})
def signup(request):
    return HttpResponse("hello world")
