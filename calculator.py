from tkinter import *

root=Tk()
root.title("My Calculator")
root.geometry("250x400+300+200")
root.resizable(0,0)

display=Entry(root,bd=20,justify="right",font=("Ariel",12))
display.grid(row=0,columnspan=4)
btn7=Button(root,text="7",font=("Ariel",12),bd=15).grid(row=1,column=0)
btn8=Button(root,text="8",font=("Ariel",12),bd=15).grid(row=1,column=1)
btn9=Button(root,text="9",font=("Ariel",12),bd=15).grid(row=1,column=2)
btn_add=Button(root,text="+",font=("Ariel",12),bd=15).grid(row=1,column=3)


btn4=Button(root,text="4",font=("Ariel",12),bd=15).grid(row=2,column=0)
btn5=Button(root,text="5",font=("Ariel",12),bd=15).grid(row=2,column=1)
btn6=Button(root,text="6",font=("Ariel",12),bd=15).grid(row=2,column=2)
btn_sub=Button(root,text="-",font=("Ariel",12),bd=15).grid(row=2,column=3)
mainloop()