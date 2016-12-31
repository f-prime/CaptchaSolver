from PIL import Image
from pytesseract import image_to_string

def getLetters(image):
    img = Image.open(image)
    width = img.width
    height = img.height
    for w in range(width): # Turn RED and WHite
        for h in range(height):
            pixel = img.getpixel((w, h))
            if pixel[0] < 50 and pixel[1] < 50 and pixel[2] < 50:
                img.putpixel((w,h), (255,0,0))
            else:
                img.putpixel((w,h), (255,255,255))
    return image_to_string(img)


print getLetters("captcha.jpg")
