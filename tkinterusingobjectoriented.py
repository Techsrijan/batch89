sfrom tkinter import *



class MyPage:
    def __init__(self,windows):
        self.button = Button(windows, text="click me object",command=self.msg).pack()

    def msg(self):
        print("Good morning")



root=Tk()
s=MyPage(root)
mainloop()