import tkinter  # imports Tkinter module

root = tkinter.Tk()  # creates a root window to place an entry with validation there


def only_numeric_input(P):
  # checks if entry's value is an integer or empty and returns an appropriate boolean
   if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
       return True
   return False
my_entry = tkinter.Entry(root)  # creates an entry
my_entry.grid(row=0, column=0)  # shows it in the root window using grid geometry manager
callback = root.register(only_numeric_input)  # registers a Tcl to Python callback
my_entry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation



def only_Alpha(P):
    if P.isalpha() or P=="":
        return True
    return False

my_entry1 = tkinter.Entry(root)  # creates an entry
my_entry1.grid(row=1, column=0)  # shows it in the root window using grid geometry manager
callback1 = root.register(only_Alpha)  # registers a Tcl to Python callback
my_entry1.configure(validate="key", validatecommand=(callback1, "%P"))  # enables validation

root.mainloop()  # enters to Tkinter main event loop