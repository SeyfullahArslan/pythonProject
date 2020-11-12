import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image
import xlsxwriter


def get_pixel_values():  # Görüntünün piksel değerlerini diziye alan fonksiyon
    image = Image.open(v.get())
    image.show()

    pixels = image.load()
    width, height = image.size
    all_pixels = []
    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            all_pixels.append(pixel)
    write_pixel_to_excel(all_pixels)


def write_pixel_to_excel(
        all_pixels):  # Dizideki piksel r,g,b değerlerini excel dosyasına farklı sütunlara yazan fonksiyon
    workbook = xlsxwriter.Workbook('HistogramOutput.xlsx')
    worksheet = workbook.add_worksheet("Image(R, G, B)")
    row = 0
    col = 0
    for value in all_pixels:
        red = value[0]
        green = value[1]
        blue = value[2]
        worksheet.write(row, col, red)
        worksheet.write(row, col + 1, green)
        worksheet.write(row, col + 2, blue)
        row += 1
    workbook.close()
    print("Values are saved successfully")


def open_dialog():  # Dosya seçimi yapılan diyalog penceresini açan fonksiyon
    filename = askopenfilename()
    v.set(filename)


# Tkinter kütüphanesi ile form penceresini oluşturan bölüm
master = tk.Tk()
top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

input_path = tk.Label(top_frame, text="Image File Path:")
v = tk.StringVar()
v.set("")
input_entry = tk.Entry(top_frame, text=v, width=40)
browse1 = tk.Button(top_frame, text="Browse", command=open_dialog)

begin_button = tk.Button(bottom_frame, text='Write to Excel', command=get_pixel_values)

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

begin_button.pack(pady=20, fill=tk.X)

master.mainloop()
