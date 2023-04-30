from tkinter import *
from tkinter import ttk
# Geometry Grid Manager
# https://tkdocs.com/tutorial/grid.html
# the geometry manager determines where widgets are placed. 

# ***Important: the pack() method is depricated
# *** use grid() method ***
# use the grid() method to tell the geometry manager what child to manage within the parent

# Grid example

# create the frame, parent widget, label, and entry widget
root = Tk()
content = ttk.Frame(root, padding=(3,3,12,12)) # apply padding inside the frame
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=200)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

# create variables for checkboxes
onevar = BooleanVar(value=True)
twovar = BooleanVar(value=False)
threevar = BooleanVar(value=True)

# create buttons
one = ttk.Checkbutton(content, text="one", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

# apply the grid() geometry manager to place the widgets on the screen
# *Tip: run each line one by one to see how the geometry manager works
# sticky: widet will "stick" to all edges of the cell
content.grid(column=0, row=0, sticky=(N,S,E,W)) 
frame.grid(column=0, row=0, columnspan=3, rowspan=3, sticky=(N,S,E,W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N,W),padx=5)
name.grid(column=3, row=1, columnspan=2, sticky=(N,E,W), pady=5, padx=5)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

# use columnconfigure and rowconfigure methods to add padding around an entire row
# the weight option tells the grid how much the col or row shold grow if there is...
# ...extra room in the master to fill. default is 0
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()


