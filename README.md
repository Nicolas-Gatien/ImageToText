# Image -> Ascii Art
If you ever wanted to make Ascii art from images, this Python script allows you to do just that!

Imagine Input            |  Screenshoted Text Output
:-------------------------:|:-------------------------:
![](https://media.discordapp.net/attachments/568505485351845904/962133654895726592/Pasted_image_20220408181246.png) |  ![](https://media.discordapp.net/attachments/568505485351845904/962133655147380736/Pasted_image_20220408181252.png?width=511&height=670)
# Instalation
1. Download The Repository
2. Navigate to where the ```imageTexter.py``` is located

# How To Use
1. Download the desired image and replace Image.jpg
2. Open CMD and navigate to  ```imageTexter.py```
3. When running the script, there are 4 variables you must enter ```C:\Users\polar\Desktop\ImageToText>imageTexter.py height width black character_repeat_amount```
4. Enter how many characters tall you want the final output to be
```C:\Users\polar\Desktop\ImageToText>imageTexter.py 100```
5. Enter how many characters wide you want the final output to be
```C:\Users\polar\Desktop\ImageToText>imageTexter.py 100 100```
6. The image will be automatically scaled to fit within these dimensions, these act as barriers / wall to limit how big the final output will be. The final dimensions may be smaller but won't ever exceed the specified dimensions.
7. If you want it to be coloured, type ```colour``` afterwards. This only works if your terminal supports python colour codes. If you want to use emojis instead of regular characters, type ```emoji```. If not either of those, type any other word
8. The last number determines how many times a character is typed out after it is chosen. This is to account for the fact that characters are taller than they are wide + empty space between rows. I've found 2 characters works best.
```C:\Users\polar\Desktop\ImageToText>imageTexter.py 100 100 black 2```
9. Press enter and it will output the text
