import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image
import PIL


def convert_to_gray(image): #Piksel tabanlı işlem ile görüntüyü grayscale forma çeviren fonksiyon
    res = PIL.Image.new(image.mode, image.size)
    width, height = image.size

    for i in range(0, width):
        for j in range(0, height):
            pixel = image.getpixel((i, j))
            avg = (pixel[0] + pixel[1] + pixel[2]) // 3
            res.putpixel((i, j), (avg, avg, avg))
    res.show()

    return res


def get_pixel_values(): #Görüntünün piksel değerlerini diziye alan fonksiyon
    colored_image = Image.open(v.get())
    colored_image.show()

    image = convert_to_gray(colored_image)

    pixels = image.load()
    width, height = image.size
    all_pixels = []
    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            all_pixels.append(pixel)
    write_pixel_to_excel(all_pixels)


def write_pixel_to_excel(all_pixels): #Dizideki piksel değerlerini excel dosyasına yazan fonksiyon
    with open('output.xls', 'w+') as f:
        f.write(' R , G , B\n')
        for value in all_pixels:
            red = value[0]
            green = value[1]
            blue = value[2]
            f.write('{0},{1},{2}\n'.format(red, green, blue))
    print("Values are saved successfully")


def open_dialog(): #Dosya seçimi yapılan diyalog penceresini açan fonksiyon
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

begin_button = tk.Button(bottom_frame, text='Convert and Write to Excel', command=get_pixel_values)

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

begin_button.pack(pady=20, fill=tk.X)

master.mainloop()
