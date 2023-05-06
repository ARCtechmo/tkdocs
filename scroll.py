# more on Widgets
# https://tkdocs.com/tutorial/morewidgets.html
from tkinter import *
from tkinter import ttk

# scrollbar 
root = Tk()
lbox = Listbox(root, height=5)
lbox.grid(column=0,row=0,sticky=(N,W,E,S))
scr = ttk.Scrollbar(root, orient=VERTICAL, command=lbox.yview)
scr.grid(column=1,row=0,sticky=(N,S))
lbox['yscrollcommand'] = scr.set
ttk.Label(root, text="Status message here", anchor=(W)).grid(
        column=0, 
        columnspan=2, 
        row=1, 
        sticky=(W,E))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
for i in range(1,101):
    lbox.insert('end','Line %d of 100' % i)

root.mainloop()
