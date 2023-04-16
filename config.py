from tkinter import *
from tkinter import ttk
root = Tk()

button = ttk.Button(root,text="Hello World!",command="buttonpressed")
button.grid()

# check the current value of the text option
# print(button['text'])

# change the value of the button
button['text'] = 'goodbye'
# print(button['text'])

# another way to do the same thing
button.configure(text='goodbye')
# print(button['text'])

# get all information about the text option
# print(button.configure('text'))

# get all information on the configuration options for this widget
# http://tkdocs.com/tutorial/concepts.html#widgets
# the first and fifth values are the most important
# objects name and the value of it
for k,v in button.configure().items():
    print(k,v)

# widget hierarchy
# http://tkdocs.com/tutorial/concepts.html#widgets
def print_hierarchy(w, depth=0):
    print('  '*depth + w.winfo_class() + 
          ' w=' + str(w.winfo_width()) + 
          ' h=' + str(w.winfo_height()) + 
          ' x=' + str(w.winfo_x()) + 
          ' y=' + str(w.winfo_y()))
    for i in w.winfo_children():
        print_hierarchy(i, depth+1)
print(print_hierarchy(root))


