from tkinter import *
root=Tk()
root.title("MY GUI")
lable=Label(root,bg="red",fg="white",text="Enter Your Name",font=("Ariel",12)).pack(side=LEFT,fill=Y)
#lable.pack()
btn=Button(root,text="Button1")
btn.pack(side=BOTTOM)
btn1=Button(root,text="Button2").pack(side=LEFT)
name=Entry(root,font=("Ariel",12),bd=20,justify="right").pack()
root.geometry("400x500+500+200")
root.resizable(0,0)
mainloop()


