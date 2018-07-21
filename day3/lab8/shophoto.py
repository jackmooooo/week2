from PIL import Image
from PIL import ImageFilter

def directory(input1):
    if input1 == "filter":
        inputnew = input("what filter  >> ")
        if inputnew == "invert":
            a = input("file name  >> ")
            inverter(a)
        elif inputnew == "darken":
            a = input("file name  >> ")
            darkener(a)
        elif inputnew == "brighten":
            a = input("file name  >> ")
            brightener(a)
        elif inputnew == "grey scale":
            a = input("file name  >> ")
            greyscaler(a)
        elif inputnew == "posterize":
            a = input("file name  >> ")
            posterizer(a)
    elif input1 == "crop":
        a = input("file  >> ")
        b = int(input("start height  >> "))
        c = int(input("end height  >> "))
        d = int(input("start width  >> "))
        e = int(input("end width  >> "))
        crop(a, b, c, d, e)
    elif input1 == "blur":
        a = input("file  >> ")
        b = input("radius  >> ")
        blur(a, b)
    elif input1 == "sharpen":
        a = input("file  >> ")
        b = int(input("radius  >> "))
        c = int(input("percentage  >> "))
        d = int(input("threshohld  >> "))
        sharpen(a, b, c, d)

def lesscolors(n):
    if n > 0 & n < 25:
        return 12
    elif n >= 25 & n < 50:
        return 37
    elif n >= 50 & n < 75:
        return 62
    elif n >= 75 & n < 100:
        return 87
    elif n >= 100 & n < 125:
        return 112
    elif n >= 125 & n < 150:
        return 137
    elif n >= 150 & n < 175:
        return 162
    elif n >= 175 & n < 200:
        return 187
    elif n >= 200 & n < 225:
        return 212
    elif n >= 225 & n < 250:
        return 237
    elif n >= 225 & n < 255:
        return 239
    else:
        return 0

def solaredpix(n):
    if n < 128:
        return 255-n
    else:
        return n

def ifclue(r, g, b):
    if r == 255 :
        if g == 255 & b == 255:
            return (0, 0, 0)
        elif g == 0 & b == 0:
            return (0, 0, 0)
    else:
        return (r, g, b)

def no_red(name):
    img = Image.open(name)
    pixels = [(0, g, b) for (r, g, b) in img.getdata()]
    img.putdata(pixels)
    img.save("no_red_" + name)

def inverter(name):
    img = Image.open(name)
    if name.count("png") == 0:
        pixels = [(255-r, 255-g, 255-b) for (r, g, b) in img.getdata()]
    else:
        pixels = [(255-r, 255-g, 255-b, a) for (r, g, b, a) in img.getdata()]
    img.putdata(pixels)
    img.save("inverted_" + name)

def darkener(name):
    img = Image.open(name)
    if (name.split(".")).count("png") == 0:
        pixels = [(int(r*0.75), int(g*0.75), int(b*0.75), a) for (r, g, b, a) in img.getdata()]
    else:
        pixels = [(int(r*0.75), int(g*0.75), int(b*0.75)) for (r, g, b) in img.getdata()]
    img.putdata(pixels)
    img.save("darkened_" + name)

def brightener(name):
    img = Image.open(name)
    if (name.split(".")).count("png") == 0:
        pixels = [(int(r*1.10), int(g*1.10), int(b*1.10), a) for (r, g, b, a) in img.getdata()]
    else:
        pixels = [(int(r*1.10), int(g*1.10), int(b*1.10)) for (r, g, b) in img.getdata()]
    img.putdata(pixels)
    img.save("brightened_" + name)

def greyscaler(name):
    img = Image.open(name)
    if (name.split(".")).count("png") == 0:
        pixels = [(int((r+g+b)/3), int((r+g+b)/3), int((r+g+b)/3), a) for (r, g, b, a) in img.getdata()]
    else:
        pixels = [(int((r+g+b)/3), int((r+g+b)/3), int((r+g+b)/3)) for (r, g, b) in img.getdata()]
    img.putdata(pixels)
    img.save("grey_ " + name)

def posterizer(name):
    img = Image.open(name)
    if (name.split(".")).count("png") == 0:
        pixels = [(lesscolors(r), lesscolors(g), lesscolors(b), a) for (r, g, b, a) in img.getdata()]
    else:
        pixels = [(lesscolors(r), lesscolors(g), lesscolors(b)) for (r, g, b) in img.getdata()]
    img.putdata(pixels)
    img.save("posterized_ " + name)

def solarizer(name):
    img = Image.open(name)
    if (name.split(".")).count("png") == 0:
        pixels = [(solaredpix(r), solaredpix(g), solaredpix(b), a) for (r, g, b, a) in img.getdata()]
    else:
        pixels = [(solaredpix(r), solaredpix(g), solaredpix(b)) for (r, g, b) in img.getdata()]
    img.putdata(pixels)
    img.save("solarized_" + name)

def crop(name, top, bottom, left, right):
    img = Image.open(name)
    pixels = img.getdata()
    pixels.crop([left, top, right, bottom])
    img.putdata(pixels)
    img.save("cropped_" + name)

def blur(name, rad):
    oldimg = Image.open(name)
    newimg = oldimg.filter(ImageFilter.GaussianBlur(radius=int(rad)))
    newimg.save("blury_" + name)

def sharpen(name, r, p, t):
    img = Image.open(name)
    newimg = img.filter(ImageFilter.UnsharpMask)
    newimg.save("sharpened_" + name)

def denoisergb(name):
    img = Image.open(name)
    pixels = [(r*10, 0, 0, a) for (r, g, b, a) in img.getdata()]
    img.putdata(pixels)
    img.save("denoised_" + name)

def denoiserr(name):
    img = Image.open(name)
    pixels = [(0, g*10, b*10, a) for (r, g, b, a) in img.getdata()]
    img.putdata(pixels)
    img.save("denoised_" + name)

def denoiserclue(name):
    img = Image.open(name)
    pixels = [ifclue(r, g, b) for (r, g, b) in img.getdata()]
    img.putdata(pixels)
    img.save("denoised_" + name)

banana = input("filter, blur, sharpen or crop  >> ")

directory(banana)
