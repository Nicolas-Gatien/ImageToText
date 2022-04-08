from tokenize import String
from PIL import Image
from math import sqrt
imag = Image.open("Image.jpg")
#Convert the image te RGB if it is a .gif for example
imag = imag.convert ('RGB')
#coordinates of the pixel

console_width = 287
console_height = 9999

while (imag.height > console_height):
    imag = imag.resize(((int)(imag.width * 0.95), (int)(imag.height * 0.95)))

while (imag.width > console_width):
    imag = imag.resize(((int)(imag.width * 0.95), (int)(imag.height * 0.95)))

for y in range(imag.height):
    output = ""
    for x in range(imag.width):
        #Get RGB
        pixelRGB = imag.getpixel((x,y))
        R,G,B = pixelRGB 
        brightness = sqrt(0.299*(R**2) + 0.587*(G**2) + 0.114*(B**2)) ##0 is dark (black) and 255 is bright (white)
        x += 1
        if R - 75 > G and R - 75 > B:
            output += "\033[1;31;40m"
        elif G - 75 > R and G - 75 > B:
            output += "\033[1;32;40m"
        elif B - 75 > R and B - 75 > G:
            output += "\033[1;34;40m"
        elif R > B and G > B:
            output += "\033[1;33;40m"
        elif R > G and B > G:
            output += "\033[1;35;40m"
        elif G > R and B > R:
            output+= "\033[1;36;40m"
        elif R > G and R > B:
            output += "\033[1;31;40m"
        elif G > R and G > B:
            output += "\033[1;32;40m"
        elif B > R and B > G:
            output += "\033[1;34;40m"

        if brightness >= 224:
            output += "@@"
        elif brightness >= 208:
            output += "&&"
        elif brightness >= 192:
            output += "BB"
        elif brightness >= 176:
            output += "GG"
        elif brightness >= 160:
            output += "OO"
        elif brightness >= 144:
            output += "UU"
        elif brightness >= 128:
            output += "##"
        elif brightness >= 112:
            output += "oo"
        elif brightness >= 96:
            output += "ee"
        elif brightness >= 80:
            output += "++"
        elif brightness >= 64:
            output += "<>"
        elif brightness >= 48:
            output += ";;"
        elif brightness >= 32:
            output += ",,"
        elif brightness >= 16:
            output += ".."
        else:
            output += "  "
        
    y += 1
    print(f"{output}")