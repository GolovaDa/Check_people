import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk


def select_file():
    file_path=filedialog.askopenfilename()
    
    if file_path=="":
        pass
    else:
        label.config(text=file_path)
        image=Image.open(file_path)
            
        image.thumbnail((600,300))
        photo=ImageTk.PhotoImage(image)
        preview.config(image=photo)
        preview.image=photo
        start.config(state="normal",bg="green")

window= tk.Tk()
window.title("Check people")


label=tk.Label(window, text="Выберите файл для обработки")
label.pack(pady=15)
preview=tk.Label(window)
preview.pack()

buttons=tk.Frame(window)

button=tk.Button(buttons,text="Выбрать файл", command=select_file)
button.pack(side="right",padx=10)
start=tk.Button(buttons,text="Начать обработку",state="disabled")
start.pack(side="left",padx=10)
buttons.pack(pady=15)
window.geometry("800x500")


window.mainloop()