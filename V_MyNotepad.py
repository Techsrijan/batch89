from tkinter import *
from tkinter import filedialog, colorchooser
import datetime

master=Tk()
class NotePad_Soft:
    current_open_file=""
    #File menu options methods
    def New_menu(self):
        self.root.title("Untitled - Notepad")
        self.file = None
        self.txt.delete(1.0,END)


    def NewWindow_menu(self):
        top= Toplevel(self.root)
        top.mainloop()


    def Open_menu(self,event=""):
        self.txt.delete(1.0,END)

        open_m= filedialog.askopenfile(initialdir="/",title="Open File",
                           filetypes=(("text files","*.txt"),("All files","*.*")))
        #print(open_m)
        for data in open_m:
            self.txt.insert(INSERT,data)
            #print(data)
        self.current_open_file=open_m.name


    def Save_menu(self,event=""):
        print(run.current_open_file)
        if self.current_open_file == "":
            self.SaveAs_menu()
        else:
            f = open(self.current_open_file, mode="a")
            f.write(self.txt.get(1.0, END))
            f.close()

    def SaveAs_menu(self,event=""):
        save_as=filedialog.asksaveasfile(mode="w", defaultextension=".txt")

        if save_as is None:
            return

        s=self.txt.get(1.0,END)
        save_as.write(s)
        save_as.close()


    def PageSetup_menu(self):
        self.txt.insert(INSERT,"ispe Kam abhi baki hai mere dost")

    def Print_menu(self):
        self.txt.insert(INSERT, "ispe Kam abhi baki hai mere dost")

    #Edit Menu options methods
    def Cut_menu(self):
        self.Copy_menu()
        self.txt.delete("sel.first","sel.last")

    def Copy_menu(self):
        self.txt.clipboard_clear()
        self.txt.clipboard_append(self.txt.selection_get())

    def Paste_menu(self):
        self.txt.insert(INSERT,self.txt.clipboard_get())


    def Delete_menu(self):
        self.txt.delete("sel.first","sel.last")

    def Search_menu(self):
        self.txt.insert(INSERT, "ispe Kam abhi baki hai mere dost")

    def Find_menu(self):
        self.txt.insert(INSERT, "ispe Kam abhi baki hai mere dost")

    def FindN_menu(self):
        self.txt.insert(INSERT, "ispe Kam abhi baki hai mere dost")

    def FindP_menu(self):
        self.txt.insert(INSERT,"ispe Kam abhi baki hai mere dost")

    def Replace_menu(self):
        self.txt.insert(INSERT,"ispe Kam abhi baki hai mere dost")

    def Goto_menu(self):
        self.txt.insert(INSERT,"ispe Kam abhi baki hai mere dost")

    def SelectAll_menu(self):
        self.txt.insert(INSERT,"ispe Kam abhi baki hai mere dost")

    def TimeDate_menu(self):

        self.x = datetime.datetime.now()
        self.txt.insert(INSERT,self.x)


    #Format menu options method
    """def WordWrap_menu(self):
        self.txt.insert(INSERT,"ispe Kam abhi baki hai mere dost")

    def Font_menu(self):
        self.txt.insert(INSERT,"ispe Kam abhi baki hai mere dost")"""

    #View Menu options method
    """def Zoom_menu(self):
        self.txt.insert(INSERT,"ispe Kam abhi baki hai mere dost")

    def StatusBar_menu(self):
        self.txt.insert(INSERT,"ispe Kam abhi baki hai mere dost")"""


    """#Help Menu options method
    def Help_menu(self):
        print("ispe Kam abhi baki hai mere dost")

    def SendFeedback_menu(self):
        print("ispe Kam abhi baki hai mere dost")

    def About_menu(self):
        print("ispe Kam abhi baki hai mere dost")"""



    def BackgroundColor_menu(self):
        clrr= colorchooser.askcolor(title="Choose Background Color")
        #print(clrr)
        self.txt.configure(background=clrr[1])


    def ForegroundColor_menu(self):
        clrr= colorchooser.askcolor(title="Choose Text Color")
        #print(clrr)
        self.txt.configure(foreground=clrr[1])





    def __init__(self,root):
        self.root=root
        root.bind("<Control-o>",self.Open_menu)   #shortcut key for open dialog box
        root.bind("<Control-s>", self.Save_menu)  #shortcut key for SaveAs dialog box
        root.bind("<Control-d>", self.SaveAs_menu)  #shortcut key for SaveAs dialog box




        root.title("My_Notepad")

        # Create ScrollBar
        self.frame=Frame(root)
        self.scroll = Scrollbar(self.frame)
        self.scroll.pack(side=RIGHT, fill=Y)

        self.txt = Text(self.frame,yscrollcommand=self.scroll, undo=True)
        self.scroll.config(command=self.txt.yview)      #This line is used for scrolling the ScrollBar
        self.txt.pack(fill=BOTH,expand=1)
        self.frame.pack(fill=BOTH, expand=1)
        # Done ScrollBar





        self.menubar=Menu(self.frame)
        self.file = Menu(self.menubar, tearoff=0)     # create a toplevel menu File

        #FILE Menu
        self.menubar.add_cascade(label="File", menu=self.file)

        self.file.add_command(label="New", command=self.New_menu)
        self.file.add_command(label="New Window", command=self.NewWindow_menu)
        self.file.add_command(label="Open", command=self.Open_menu)
        self.file.add_command(label="Save", command=self.Save_menu)
        self.file.add_command(label="Save As", command=self.SaveAs_menu)
        self.file.add_separator()
        self.file.add_command(label="Page Setup", command=self.PageSetup_menu)
        self.file.add_command(label="Print", command=self.Print_menu)
        self.file.add_separator()
        self.file.add_command(label="Exit", command=root.quit)



        #Edit Menu
        self.edit = Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=self.edit)
        self.edit.add_command(label="Undo", command=self.txt.edit_undo)
        self.edit.add_command(label="Redo", command=self.txt.edit_redo)
        self.edit.add_separator()
        self.edit.add_command(label="Cut", command=self.Cut_menu)
        self.edit.add_command(label="Copy", command=self.Copy_menu)
        self.edit.add_command(label="Paste", command=self.Paste_menu)
        self.edit.add_command(label="Delete", command=self.Delete_menu)
        self.edit.add_separator()
        self.edit.add_command(label="Search with Bing....", command=self.Search_menu)
        self.edit.add_command(label="Find", command=self.Find_menu)
        self.edit.add_command(label="Find Next", command=self.FindN_menu)
        self.edit.add_command(label="Find Previous", command=self.FindP_menu)
        self.edit.add_command(label="Replace", command=self.Replace_menu)
        self.edit.add_command(label="Go To...", command=self.Goto_menu)
        self.edit.add_separator()
        self.edit.add_command(label="Select All", command=self.SelectAll_menu)
        self.edit.add_command(label="Time/Date", command=self.TimeDate_menu)



        #Format Menu
        """self.formatmenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="Format",menu=self.formatmenu)
        self.formatmenu.add_command(label="Word Wrap", command=self.WordWrap_menu)
        self.formatmenu.add_command(label="Font", command=self.Font_menu)"""



        #View manu
        """self.view = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="View", menu=self.view)
        self.view.add_command(label="Zoom", command=self.Zoom_menu)
        self.view.add_command(label="Status Bar", command=self.StatusBar_menu)"""



        #Help bar
        """self.help = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.help)
        self.help.add_command(label="View Help", command=self.Help_menu)
        self.help.add_command(label="Send Feedback", command=self.SendFeedback_menu)
        self.help.add_separator()
        self.help.add_command(label="About Notepad", command=self.About_menu)"""



        self.bgcolor = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Color", menu=self.bgcolor)
        self.bgcolor.add_command(label="Background Color", command=self.BackgroundColor_menu)
        self.bgcolor.add_command(label="Text Color", command=self.ForegroundColor_menu)




        #very Important -->  this lines is used for DISPLAY THE MENU
        self.root.config(menu=self.menubar)





run=NotePad_Soft(master)

master.mainloop()