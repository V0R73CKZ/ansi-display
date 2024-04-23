from PIL import Image
import math, time, sys, os, subprocess
os.system('clear')
#+str(math.floor((os.get_terminal_size()[0]/2)))+
subprocess.run(['bash', '-c', 'DISPLAY=:0 scrot old_image.png && convert old_image.png -resize '+str(math.floor((os.get_terminal_size()[0]/2)))+'x'+str(math.floor(os.get_terminal_size()[1]-1))+' image.png'])
image_path = 'image.png'
image = Image.open(image_path)
width, height = image.size
x = []
for v in range(height):
    for w in range(width):
        values = image.getpixel((w, v))
        values = list(values)
        #values.pop(3)
        x.append(values)
'''
or to make it start from the bottom left and go to the top right
do this

from PIL import Image
image_path = 'image.png'
image = Image.open(image_path)
width, height = image.size
rgb_list = []
for y in reversed(range(height)):
    for x in range(width):
        values = image.getpixel((x, y))
        values = list(values)
        values.pop(3)
        rgb_list.append(values)
print(rgb_list)
'''
num1 = 0
num2 = 0
s = "  "
a = image.size
#if this was gonna be a video, add a for loop here
for j in range(a[1]):
    for i in range(a[0]):
        if num1 == len(x):
            break
        if num2+1 == a[0]:
            print("\x1b[48;2;"+str(x[num1][0])+";"+str(x[num1][1])+";"+str(x[num1][2])+"m"+s+"\033[0m")
            num1 += 1
            num2 = 0
            break
        print("\x1b[48;2;"+str(x[num1][0])+";"+str(x[num1][1])+";"+str(x[num1][2])+"m"+s+"\033[0m",end="")
        #sys.stdout.write()
        #sys.stdout.flush()
        num1 += 1
        num2 += 1
'''
and clear this bottom part here by importing "os"
then using "os.system("clear")" here
'''
os.system('clear')
subprocess.run(['bash', '-c', 'rm image.png old_image.png'])
