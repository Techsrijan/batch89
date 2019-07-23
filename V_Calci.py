from tkinter import *
root = Tk()
root.geometry("361x381+500+150")
root.title("My Calculator")

display = Entry(root,bd=29, justify="right" ,bg="powder blue" ,font=("Ariel",20)).grid(row = 0,rowspan=1,columnspan=4)

btn_AC= Button(text="AC",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=1,column=0)
btn_back= Button(text="[X]",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=1,column=1)
btn_mod= Button(text="%",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=1,column=2)
btn_divide= Button(text="÷",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=1,column=3)



btn7= Button(text="7",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=2,column=0)
btn8= Button(text="8",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=2,column=1)
btn9= Button(text="9",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=2,column=2)
btn_mul= Button(text="x",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=2,column=3)


btn4= Button(text="4",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=3,column=0)
btn5= Button(text="5",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=3,column=1)
btn6= Button(text="6",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=3,column=2)
btn_sub= Button(text="-",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=3,column=3)



btn1= Button(text="1",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=4,column=0)
btn2= Button(text="2",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=4,column=1)
btn3= Button(text="3",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=4,column=2)
btn_add= Button(text="+",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=4,column=3)


btn_sp= Button(text="+/-",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=4,column=0)
btn0= Button(text="0",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=4,column=1)
btn_dot= Button(text=".",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=4,column=2)
btn_equal= Button(text="=",font=("Ariel",12,"bold"),bd=12, height=2, width=6).grid(row=4,column=3)






mainloop()