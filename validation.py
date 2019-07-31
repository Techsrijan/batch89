import tkinter  # imports Tkinter module


root = tkinter.Tk()  # creates a root window to place an entry with validation there

'''
# valid percent substitutions (from the Tk entry man page)
        # note: you only have to register the ones you need; this
        # example registers them all for illustrative purposes
        #
        # %d = Type of action (1=insert, 0=delete, -1 for others)
        # %i = index of char string to be inserted/deleted, or -1
        # %P = value of the entry if the edit is allowed
        # %s = value of entry prior to editing
        # %S = the text string being inserted or deleted, if any
        # %v = the type of validation that is currently set
        # %V = the type of validation that triggered the callback
        #      (key, focusin, focusout, forced)
        # %W = the tk name of the widget




'''
def only_numeric_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False

def only_char_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isalpha() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False

my_entry = tkinter.Entry(root)  # creates an entry
my_entry.grid(row=0, column=0)  # shows it in the root window using grid geometry manager

my_entry1 = tkinter.Entry(root)  # creates an entry
my_entry1.grid(row=1, column=0)  # shows it in the root window using grid geometry manager
callback = root.register(only_char_input)  # registers a Tcl to Python callback
callback1 = root.register(only_numeric_input)  # registers a Tcl to Python callback

my_entry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation
my_entry1.configure(validate="key", validatecommand=(callback1, "%P"))n
root.mainloop()  # enters to Tkinter main event loop