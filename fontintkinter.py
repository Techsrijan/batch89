from tkinter import *
from tkinter.font import Font

root=Tk()
my_font=Font(family="Helvetica",size=24,weight="bold",slant="italic",underline=1,overstrike=1)
'''fonts=list(())
for i in fonts:
    print(i)'''


txt=Text(root,height=5,width=30,font=my_font,wrap=WORD,padx=10,pady=10,bd=5,selectbackground="red")
txt.insert(INSERT,"Welcome you all")
txt.pack()

mainloop()