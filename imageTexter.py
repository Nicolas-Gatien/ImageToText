from tokenize import String
from PIL import Image
from math import sqrt
import sys

# Get Image
imag = Image.open("Image.jpg") 
imag = imag.convert ('RGB')

console_width = 287
console_height = 9999

console_width = int(sys.argv[1])
console_height = int(sys.argv[2])

colour = False
emoji = False
repeatCount = int(sys.argv[4])


if sys.argv[3] == "colour":
    colour = True
elif sys.argv[3] == "emoji":
    emoji = True

# Resize Image to fit in console
while (imag.height > console_height):
    imag = imag.resize(((int)(imag.width * 0.95), (int)(imag.height * 0.95)))

while (imag.width > console_width / repeatCount):
    imag = imag.resize(((int)(imag.width * 0.95), (int)(imag.height * 0.95)))

def AddToOutput(character):
    tempOutput = ""

    for x in range(repeatCount):
        tempOutput += f"{character}"
    
    return tempOutput

# For each Row
for y in range(imag.height):
    output = ""
    # Loop through each pixel in that row
    for x in range(imag.width):
        pixelRGB = imag.getpixel((x,y)) # Get Pixel info
        R,G,B = pixelRGB 
        brightness = sqrt(0.299*(R**2) + 0.587*(G**2) + 0.114*(B**2)) ##0 is dark (black) and 255 is bright (white)

        # Loop through each pixel in the row
        x += 1
        if colour == True:
            if R - 75 > G and R - 75 > B: # If it is mostly Red, set it red
                output += "\033[1;31;40m"
            elif G - 75 > R and G - 75 > B: # Mostly Green, set it green
                output += "\033[1;32;40m"
            elif B - 75 > R and B - 75 > G: # Mostly Blue, set it blue
                output += "\033[1;34;40m"
            elif R > B and G > B: # Colour Mixes
                output += "\033[1;33;40m"
            elif R > G and B > G:
                output += "\033[1;35;40m"
            elif G > R and B > R:
                output+= "\033[1;36;40m"
            elif R > G and R > B: # Default Colours
                output += "\033[1;31;40m"
            elif G > R and G > B:
                output += "\033[1;32;40m"
            elif B > R and B > G:
                output += "\033[1;34;40m"

        # Determine the Character that will be written based on brightness of pixel
        if emoji == True:
            if brightness >= 224:
                output += AddToOutput("🏐")
            elif brightness >= 208:
                output += AddToOutput("📰")
            elif brightness >= 192:
                output += AddToOutput("📖")
            elif brightness >= 176:
                output += AddToOutput("📋")
            elif brightness >= 160:
                output += AddToOutput("☕")
            elif brightness >= 144:
                output += AddToOutput("🎳")
            elif brightness >= 128:
                output += AddToOutput("🥌")
            elif brightness >= 112:
                output += AddToOutput("💾")
            elif brightness >= 96:
                output += AddToOutput("🗿")
            elif brightness >= 80:
                output += AddToOutput("💿")
            elif brightness >= 64:
                output += AddToOutput("📓")
            elif brightness >= 48:
                output += AddToOutput("📺")
            elif brightness >= 32:
                output += AddToOutput("🎓")
            elif brightness >= 16:
                output += AddToOutput("🎥")
            else:
                output += AddToOutput("💣")
        else
            if brightness >= 224:
                output += AddToOutput("@")
            elif brightness >= 208:
                output += AddToOutput("&")
            elif brightness >= 192:
                output += AddToOutput("B")
            elif brightness >= 176:
                output += AddToOutput("G")
            elif brightness >= 160:
                output += AddToOutput("O")
            elif brightness >= 144:
                output += AddToOutput("U")
            elif brightness >= 128:
                output += AddToOutput("#")
            elif brightness >= 112:
                output += AddToOutput("o")
            elif brightness >= 96:
                output += AddToOutput("e")
            elif brightness >= 80:
                output += AddToOutput("+")
            elif brightness >= 64:
                output += AddToOutput("-")
            elif brightness >= 48:
                output += AddToOutput(";")
            elif brightness >= 32:
                output += AddToOutput(",")
            elif brightness >= 16:
                output += AddToOutput(".")
            else:
                output += AddToOutput(" ")
        


    # Print Row
    print(f"{output}")
    # Next Row
    y += 1

