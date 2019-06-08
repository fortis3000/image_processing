import cv2
import numpy as np
from tkinter import Tk, Canvas, Scale, Label, HORIZONTAL
from PIL import ImageTk, Image

def getValue(scale):
    return(scale.get())

def scaleHandler(root):
    imgs.clear()
    h_min = getValue(scale_hmin)
    h_max = getValue(scale_hmax)
    s_min = getValue(scale_smin)
    s_max = getValue(scale_smax)
    v_min = getValue(scale_vmin)
    v_max = getValue(scale_vmax)
    lower_red = np.array([h_min,s_min,v_min])
    upper_red = np.array([h_max,s_max,v_max])
    image_filtered = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image_filtered = cv2.inRange(image_filtered, lower_red, upper_red)
    image_filtered = ImageTk.PhotoImage(Image.fromarray(image_filtered))
    canvas.delete('all')
    canvas.create_image(250,250, image=image_filtered)
    imgs.append(image_filtered)
    
root = Tk()
window_width = 500
window_length = 950
root.geometry(str(window_width) + 'x' + str(window_length))

global image
path=input().strip('"')

try:
    image = cv2.imread(path)
    koef = min(image.shape[0], image.shape[1])/400
    image = cv2.resize(image, (int(image.shape[1]/koef), int(image.shape[0]/koef)))
    image1 = ImageTk.PhotoImage(Image.fromarray(image))
except AttributeError:
    exit()

#промежуточное сохранение обработанного изображения (без него не показывает)
global imgs
imgs = []

# перерисовка канвас из обработчка ползунка
global canvas
canvas = Canvas(root,width=600,height=600)
imagesprite = canvas.create_image(0,0, image=image1)

# перменные для текущих значений ползунков HSV
global h_min
global h_max
global s_min
global s_max
global v_min
global v_max

# максимальные значения для цветовых измерений
h_uplimit = 179
s_uplimit = 255
v_uplimit = 255
scale_hmin = Scale(root,
               orient=HORIZONTAL,
               width=10,
               length=300,
               from_=0,
               to=h_uplimit,
               tickinterval=30,
               resolution=1,
               command=scaleHandler)
scale_hmax = Scale(root,
               orient=HORIZONTAL,
               width=10,
               length=300,
               from_=0,
               to=h_uplimit,
               tickinterval=30,
               resolution=1,
               command=scaleHandler)
scale_smin = Scale(root,
               orient=HORIZONTAL,
               width=10,
               length=300,
               from_=0,
               to=s_uplimit,
               tickinterval=30,
               resolution=1,
               command=scaleHandler)
scale_smax = Scale(root,
               orient=HORIZONTAL,
               width=10,
               length=300,
               from_=0,
               to=s_uplimit,
               tickinterval=30,
               resolution=1,
               command=scaleHandler)
scale_vmin = Scale(root,
               orient=HORIZONTAL,
               width=10,
               length=300,
               from_=0,
               to=v_uplimit,
               tickinterval=30,
               resolution=1,
               command=scaleHandler)
scale_vmax = Scale(root,
               orient=HORIZONTAL,
               width=10,
               length=300,
               from_=0,
               to=v_uplimit,
               tickinterval=30,
               resolution=1,
               command=scaleHandler)

# установка начальных значений
scale_hmax.set(h_uplimit)
scale_smax.set(s_uplimit)
scale_vmax.set(v_uplimit)

label_h = Label(text = 'Hue - цвет', font='Ubuntu 12')
label_s = Label(text= 'Saturation - насыщенность', font='Ubuntu 12')
label_v = Label(text= 'Value (brightness) - яркость', font='Ubuntu 12')

# размещение в окне
label_h.pack()
scale_hmin.pack()
scale_hmax.pack()
label_s.pack()
scale_smin.pack()
scale_smax.pack()
label_v.pack()
scale_vmin.pack() 
scale_vmax.pack()
canvas.pack()

root.mainloop()