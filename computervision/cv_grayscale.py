import tkinter as tk
from tkinter.filedialog import askopenfilename
import cv2
import PIL
from PIL import Image


def convert_to_gray():
    image = Image.open(v.get())
    res = PIL.Image.new(image.mode, image.size)
    width, height = image.size

    for i in range(0, width):
        for j in range(0, height):
            pixel = image.getpixel((i, j))
            avg = (pixel[0] + pixel[1] + pixel[2]) // 3
            res.putpixel((i, j), (avg, avg, avg))
    res.show()
    image.show()


def open_dialog():
    filename = askopenfilename()
    v.set(filename)


master = tk.Tk()
top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

input_path = tk.Label(top_frame, text="Image File Path:")
v = tk.StringVar()
v.set("")
input_entry = tk.Entry(top_frame, text=v, width=40)
browse1 = tk.Button(top_frame, text="Browse", command=open_dialog)

begin_button = tk.Button(bottom_frame, text='Convert', command=convert_to_gray)

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

begin_button.pack(pady=20, fill=tk.X)

master.mainloop()
