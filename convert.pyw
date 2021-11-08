from tkinter import *
from tkinter import messagebox
from PIL import Image
from tkinter import filedialog

def convert():
    filename = entry1.get()
    img = Image.open(filename)
    img.save(filename)
    icon_sizes = [(96,96)]
    text = entry2.get()
    img.save(f'C:/Users/melih/Desktop/{text}.ico', sizes=icon_sizes)

def clear():
    entry1.delete(0,END)
    entry2.delete(0,END)

def choose():
    filename = filedialog.askopenfilename(filetypes=(("Png Files","*.png"),("All files","*.*")))
    if not (entry1 == ""):
        entry1.delete(0,END)
    entry1.insert(END,filename)


root = Tk()
root.geometry("400x150")
root.title("Png > Ico Converter")
root.resizable(width=False, height=False)

lbl1 = Label(root,text="Png Location:")
lbl2 = Label(root,text="Icon Name:")
entry1 = Entry(root,width=42)
entry2 = Entry(root,width=42)
btn1 = Button(root,text="Dosya Seç",width=10,command=choose)
btn2 = Button(root,text="Temizle",width=10,command=clear)
btn3 = Button(root,text="Dönüştür",width=10,command=convert)

lbl1.place(x=10,y=10)
lbl2.place(x=10,y=50)
entry1.place(x=120,y=10)
entry2.place(x=120,y=50)
btn1.place(x=10,y=100)
btn2.place(x=100,y=100)
btn3.place(x=190,y=100)

root.mainloop()