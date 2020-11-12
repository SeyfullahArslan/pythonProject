import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image


def get_pixel_values(): #Görüntünün piksel değerlerini diziye alan fonksiyon
    image = Image.open(v.get())
    pixels = image.load()
    width, height = image.size

    all_pixels = []
    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            all_pixels.append(pixel)
    matrix_to_vector(all_pixels)


def matrix_to_vector(all_pixels):# 3 boyutlu (R,G,B) matrisi, tek boyutlu vektöre çeviren fonksiyon
    pixel_vector = []
    for value in all_pixels:
        red = value[0]
        pixel_vector.append(red) #kırmızı kanal değerlerinin vektöre eklenmesi

    for value in all_pixels:
        green = value[1]
        pixel_vector.append(green) #yeşil kanal değerlerinin vektöre eklenmesi

    for value in all_pixels:
        blue = value[2]
        pixel_vector.append(blue) #mavi kanal değerlerinin vektöre eklenmesi

    for vector_value in pixel_vector:
        print(vector_value)


def open_dialog():#Dosya seçimi yapılan diyalog penceresini açan fonksiyon
    filename = askopenfilename()
    v.set(filename)

#Tkinter kütüphanesi ile form penceresini oluşturan bölüm
master = tk.Tk()
top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

input_path = tk.Label(top_frame, text="Image File Path:")
v = tk.StringVar()
v.set("")
input_entry = tk.Entry(top_frame, text=v, width=40)
browse1 = tk.Button(top_frame, text="Browse", command=open_dialog)

begin_button = tk.Button(bottom_frame, text='Convert Matrix to Vector', command=get_pixel_values)

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

begin_button.pack(pady=20, fill=tk.X)

master.mainloop()
