# http://tkdocs.com/tutorial/concepts.html#events
# use command callbacks or event bindings to handle some event (click button)

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("event handler")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

# callbacks
# use the command callback as a parameter in the function
# keep it simple - your callback should simply call some other procedure
def calculate(*args):
    # code to do perform calculation
    pass
ttk.Button(mainframe, text="Calculate", command=calculate)


# Binding Events
# use functions most of the time...
# but you can use bindings to capture one-off trivial callbacks
# Tkinter expects you to provide a function as the event callback...
# whose first argument is an event object representing the event that triggered the callback..
# and the second argument is Python's anonymous function via lambda
# example shows a label responding to different events
l = ttk.Label(root, text="Experiment with the event hanlders (e.g. move the mouse, double click)")
l.grid()
l.focus()
l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
l.bind('<3>', lambda e: l.configure(text='Clicked right mouse button'))
l.bind('<Double-1>', lambda e: l.configure(text="Double Clicked"))
l.bind('<B3-Motion>', lambda e: l.configure(text="right button drag to %d,%d" % (e.x, e.y)))
root.mainloop()

