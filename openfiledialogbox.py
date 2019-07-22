from tkinter import *
from tkinter import filedialog,colorchooser

def open_file(event=""):
    res=filedialog.askopenfile(initialdir="/",title="Open File",
                           filetypes=(("text files","*.txt"),("All files","*.*")))
    print(res)
    for data in res:
        print(data)

def save_file():
    f=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if f is None:
        return
    f.write("techsrijan file saved")
    f.close()


def open_color():
    color=colorchooser.askcolor(title="choose BackGround color")
    print(color)
    root.configure(background=color[1])


root=Tk()
root.bind("<Control-o>",open_file)
txt=Text(root)
btn_open=Button(root,text="Open file",command=open_file)
btn_saveas=Button(root,text="Save file",command=save_file)
btn_clr=Button(root,text="choose background color",command=open_color)
txt.pack()
btn_open.pack()
btn_saveas.pack()
btn_clr.pack()
root.geometry("400x400+400+200")

mainloop()