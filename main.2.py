import tkinter.messagebox
from tkinter import *
from tkinter import messagebox


import random
from PIL import Image

root=Tk()

root.geometry("300x300")

def get_file():
    global my_image
    file_name = input("please give file name: ")
    my_image = Image.open(file_name)
get_file()

def My_image():
    rows = my_image.size[0]
    cols = my_image.size[1]
    print(rows, "by", cols)
    px = my_image.load()
    px[9,9] = (0,0,0)


    for i in range(rows):
        start = random.randint(0, rows)
        end = random.randint(0, cols)
        nub = random.randint(1, 5)

        if i % 2 == 0:
            start = 0
        else:
            start = 1

        for j in range(start, cols, nub):
            red = random.randint(0, 0)
            #green = random.randint(0, 0)
            #blue = random.randint(0, 0)
            red_str = red_slider.get()
            red = int(red_str)
            green_str = green_slider.get()
            green = int(green_str)
            blue_str = blue_slider.get()
            blue = int(blue_str)
            px[i, j] = (red, green, blue)
    # to get more of one color, type 255 on one of these red, green, blue

    my_image.show()
#My_image()

glitch_it = Button(root, text='glitch it...', command=My_image)
glitch_it.grid(row=0, column=2)

#rgb sliders


red_slider = Scale(root, from_=0, to=255, orient=HORIZONTAL)
red_slider.grid(row=0, column=0)
green_slider = Scale(root, from_=0, to=255, orient=HORIZONTAL)
green_slider.grid(row=1, column=0)
blue_slider = Scale(root, from_=0, to=255, orient=HORIZONTAL)
blue_slider.grid(row=2, column=0)


print(green_slider.get())


root.mainloop()