from tkinter import *
from tkinter import filedialog


class text_editor:

    def open_file(self):
        f = filedialog.askopenfile(initialdir="c://", title="Select file",
                                   filetypes=(("text file", "*.txt"), ("all files", "*.*")))
    def save_file(self):
        pass
    def save_as_file(self):
        pass
    def __init__(self,master):
        self.master=master
        master.title("MyNotePAd")
        self.text_area=Text()
        self.text_area.pack(fill=BOTH,expand=1)
        self.main_menu=Menu()
        self.master.config(menu=self.main_menu)
        #creating file menu
        self.file_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="File",menu=self.file_menu)
        #to add open in file menu
        self.file_menu.add_command(label="Open",command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="SaveAs", command=self.save_as_file)
        #seprator
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)
        # creating Edit menu
        self.edit_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="Edit", menu=self.file_menu)


bob = Tk()

te =text_editor(bob)
bob.mainloop()