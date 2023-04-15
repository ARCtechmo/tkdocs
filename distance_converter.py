# feet to meters converter
# http://tkdocs.com/tutorial/firstexample.html

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Feet to Meters")

# create a frame widget
mainframe = ttk.Frame(root, padding="3 3 12 12")

# grid places the frame directly inside the main application window
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

# tell Tk that the frame should expan to fill any extra space if the window is resized
# note: the main window is separate from the "themed" widgets
# using a "themed" frame widget to hold content ensures the background is correct
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# set a global variable 
# Note: assign global varialbe to "textvariable" so Tk will automatically update the variable
feet = StringVar()

# create the entry widget and place it onscreen
# * design: entry the feet - convert to meters so the feet has an Entry widget
# When you create a widget you must specify its parent. 
# The child widget goes inside the parent widget.
# mainframe is the parent widget (first parameter of the function)
# feet_entry widet is the child and is placed inside mainframe
# configuation option: the entry is 7 characters long
# ** textvarialbe explanation:
#   -global variable feet specified as the textvariable
#   -whenever the entry changes, Tk will automatically update the global variable
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)

# grid places the widget on the screen
# sticky option decscribes how the widget should line up within the grid cell
# w (west) means anchor the widget to the left side of the cell
feet_entry.grid(column=2, row=1, sticky=(W,E))

# take the feet from the entry widget, perform the calculation, and place result into the Label widget
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5 /10000.0))
    except ValueError:
        pass

# apply the same method to create more widgets
# * "textvariable" explanation:
#   -change the value for the "textvariable" associated with the widget
#   -the widget will be automatically updated with the current contents of the variable 
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W,E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# polish up the user interface
# loop is a shortcut to apply configuarations to all the widgets
# tell Tk to place the focus on our entry widget so the cursor will start in that field
# bind the return key to the calculate function 
# (i.e., when the user presses the reutrn button it will execute calculate function)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind("<Return>", calculate)


# start the event loop
root.mainloop()