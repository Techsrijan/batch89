from tkinter import *

root=Tk()
f=Frame(root)
scroll=Scrollbar(f)
scroll.pack(side=RIGHT,fill=Y)

listbox=Listbox(f,yscrollcommand=scroll)
for i in range(1,100):
    listbox.insert(END,str(i))
listbox.pack(side=LEFT)
scroll.config(command=listbox.yview)
root.geometry("400x400+400+200")
f.pack()
mainloop()