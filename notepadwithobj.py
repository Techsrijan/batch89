from tkinter import *
from tkinter import filedialog,colorchooser


class text_editor:
    current_open_file="openfile"
    def open_file(self,event=""):
        f = filedialog.askopenfile(initialdir="c://", title="Select file",
                                   filetypes=(("text file", "*.txt"), ("all files", "*.*")))
        for data in f:
            self.text_area.insert(INSERT, data)
        self.current_open_file=f.name

    def save_file(self):
        print(te.current_open_file)
        if self.current_open_file=="openfile":
            self.save_as_file()
        else:
            f = open(self.current_open_file, mode="a")
            f.write(self.text_area.get(1.0, END))
            f.close()





    def save_as_file(self):
        f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        if f is None:
            return
        s = self.text_area.get(1.0, END)
        f.write(s)
        f.close()

    def cut_file(self):
         self.copy_file()
         self.text_area.delete('sel.first','sel.last')

    def copy_file(self):
         self.text_area.clipboard_clear()
         self.text_area.clipboard_append(self.text_area.selection_get())

    def paste_file(self):
         self.text_area.insert(INSERT,self.text_area.clipboard_get())

    def change_color(self):
        color = colorchooser.askcolor(title="choose BackGround color")
        #print(color)
        self.text_area.configure(background=color[1])

    def change_fore_color(self):
        color = colorchooser.askcolor(title="choose ForeGround color")
        #print(color)
        self.text_area.configure(foreground=color[1])

    def delete_file(self):
        pass


    def __init__(self,master):
        self.master=master
        master.title("MyNotePAd")
        master.bind("<Control-o>",self.open_file)
        self.text_area=Text(self.master,undo=True)
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
        self.edit_menu = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        # to add menu in edit menu
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut_file)
        self.edit_menu.add_command(label="Copy", command=self.copy_file)
        self.edit_menu.add_command(label="Paste", command=self.paste_file)
        self.edit_menu.add_command(label="Delete", command=self.delete_file)
        self.edit_menu.add_separator()

        # creating Color menu
        self.color_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Format", menu=self.color_menu)
        # to add menu in format menu
        self.color_menu.add_command(label="BackGround color", command=self.change_color)
        self.color_menu.add_command(label="ForeGround color", command=self.change_fore_color)

bob = Tk()

te =text_editor(bob)
bob.mainloop()