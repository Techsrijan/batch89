from tkinter import *

master=Tk()
class NotePad_Soft:
    #File menu options methods
    def New_menu(self):
        print("ispe Kam abhi baki hai mere dost")

    def NewWindow_menu(self):
        print("ispe bhi Kam abhi baki hai mere dost")

    def Open_menu(self):
        print("ispe Kam abhi baki hai mere dost")

    def Save_menu(self):
        print("ispe Kam abhi baki hai mere dost")

    def SaveAs_menu(self):
            print("ispe Kam abhi baki hai mere dost")

    def PageSetup_menu(self):
        print("ispe Kam abhi baki hai mere dost")

    def Print_menu(self):
            print("ispe Kam abhi baki hai mere dost")


    #Edit Menu options methods
    def Undo_menu(self):
            print("ispe Kam abhi baki hai mere dost")

    def Cut_menu(self):
            print("ispe Kam abhi baki hai mere dost")

    def Copy_menu(self):
            print("ispe Kam abhi baki hai mere dost")
    def Paste_menu(self):
            print("ispe Kam abhi baki hai mere dost")
    def Delete_menu(self):
            print("ispe Kam abhi baki hai mere dost")
    def Search_menu(self):
            print("ispe Kam abhi baki hai mere dost")

    def Find_menu(self):
            print("ispe Kam abhi baki hai mere dost")
    def FindN_menu(self):
            print("ispe Kam abhi baki hai mere dost")

    def FindP_menu(self):
        print("ispe Kam abhi baki hai mere dost")

    def Replace_menu(self):
        print("ispe Kam abhi baki hai mere dost")

    def Goto_menu(self):
        print("ispe Kam abhi baki hai mere dost")

    def SelectAll_menu(self):
        print("ispe Kam abhi baki hai mere dost")

    def TimeDate_menu(self):
        print("ispe Kam abhi baki hai mere dost")



    #Format menu options method
    def WordWrap_menu(self):
        print("ispe Kam abhi baki hai mere dost")

    def Font_menu(self):
        print("ispe Kam abhi baki hai mere dost")

    #View Menu options method
    def Zoom_menu(self):
        print("ispe Kam abhi baki hai mere dost")

    def StatusBar_menu(self):
        print("ispe Kam abhi baki hai mere dost")


    #Help Menu options method
    def Help_menu(self):
        print("ispe Kam abhi baki hai mere dost")

    def SendFeedback_menu(self):
        print("ispe Kam abhi baki hai mere dost")

    def About_menu(self):
        print("ispe Kam abhi baki hai mere dost")




    def __init__(self,root):
        self.root=root
        root.title("Vish_Notepad")

        #self.sb= Scrollbar(root).pack(side=RIGHT, fill=Y)
        self.t = Text(root).pack(fill=BOTH,expand=1)

        self.menubar=Menu(self.root)
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
        self.edit.add_command(label="Undo", command=self.Undo_menu)
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
        self.formatmenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="Format",menu=self.formatmenu)
        self.formatmenu.add_command(label="Word Wrap", command=self.WordWrap_menu)
        self.formatmenu.add_command(label="Font", command=self.Font_menu)



        #View manu
        self.view = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="View", menu=self.view)
        self.view.add_command(label="Zoom", command=self.Zoom_menu)
        self.view.add_command(label="Status Bar", command=self.StatusBar_menu)



        #Help bar
        self.help = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.help)
        self.help.add_command(label="View Help", command=self.Help_menu)
        self.help.add_command(label="Send Feedback", command=self.SendFeedback_menu)
        self.help.add_separator()
        self.help.add_command(label="About Notepad", command=self.About_menu)





        #very Important -->  this lines is used for DISPLAY THE MENU
        self.root.config(menu=self.menubar)



run=NotePad_Soft(master)

master.mainloop()