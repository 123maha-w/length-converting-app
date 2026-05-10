from tkinter import *
window = Tk()
window.title('length converting app')
window.geometry('400x300')

lbl = Label(text = "hey there!", fg="white",bg="#072f5f",width=300,height=1)

Name_lbl = Label(text="give length",bg="#3895d3")
Name_entry = Entry()

def display():
    name = Name_entry.get()

    global Message
    Message=""
    greet = "this is the length "+name+"\ncm"

    Text_box.insert(END,greet)
    Text_box.insert(END,Message)

Text_box = Text(height=3)

btn = Button(text="begin", command = display, height=1,bg="#1261a0",fg="white")

lbl.pack()
Name_lbl.pack()
Name_entry.pack()
btn.pack()
Text_box.pack()

window.mainloop()