from tkinter import *

root=Tk()
canvas=Canvas(root,width=500,height=800,bg="yellow")
line=canvas.create_line(0,0,400,300,fill="red")
rec=canvas.create_rectangle(0,0,200,200,fill="green")
oval=canvas.create_oval(0,0,200,400,fill="orange")
points=[250,110,480,200,280,280,250,110]
poly=canvas.create_polygon(points,fill="blue",outline="white",width=5)
photo=PhotoImage(file=r"C:\Users\Ashwani\PycharmProjects\batch89\test.gif")
p=canvas.create_image(0,0,image=photo,anchor=NW)
canvas.pack()
root.geometry("400x400+400+200")

mainloop()