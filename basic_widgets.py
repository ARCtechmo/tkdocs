# basic widgets
# https://tkdocs.com/tutorial/widgets.

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Basic Widgets Examples")

# frames often act as the master widget for the geometry manager grid()
frame = ttk.Frame(root)

# adding
# use padding to get extra space around the inside of the widget
frame['padding'] = 5 # 5 pixels on all sides
frame['padding'] = (5,10) # 5 pixels left and right; 10 pixels top bottom
frame['padding'] = (5,7,10,12) # left: 5, right: 7, top: 10, bottom: 12

# borderwidth - flat (default), raised, sunken, solid, ridge, groove
# display a border around a frame widget to visually separate it from its surroundings
frame['borderwidth'] = 2
frame['relief'] = 'sunken'

# change styles - use the Style configuration method
s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
ttk.Frame(root, width=200, height=200, style='Danger.Tframe').grid()

# Label
# A label is a widet that displays text or images that users will view but interact with
label = ttk.Label(root, text='Full name:')

# variables
# **use Tk classes for variables; not normal Python variables
s = StringVar(value='abc')
b = BooleanVar(value=True)
i = IntVar(value=10)
d = DoubleVar(value=10.5)

# display text
# use label with the textvariable option to display the value of a variable
# attach widgets to an instance of the StringVar class; not Python variables
resultsContents = StringVar()
label['textvariable'] = resultsContents
resultsContents.set('New value to display') # set (read) and get (write) methods 

# display images
# two steps: to create an image
# 1. create an image object 
# 2. tell the label to use that object via its image configuration option
image = PhotoImage(file='myimage.gif')
label['image'] = image

# use the command configuration option display images and text at the same time 
# command = none (default); command = text (text only), command = image (image only)
# command = center (text in the center of an image)
# command = top (image above text); sae applies to left, bottom, and right

# fonts, colors, and more
# create a new style and use the style option
# style = TkDefaultFont, TkTextFont, etc...
label['font'] = 'TkDefaultFont'

# layout - geometry manager
# the gemometry manager determines the overall layout of the label
# use the anchor option to specify what edge or corner the label should be attached to
# anchor = e, se, s, sw, w, nw, center

# multi-line labels
# labels can display more than one line of text
# use text = "some text\n" or textvariable string or the wraplength option
# use the justify option for multiple lines justify = left, center, right

# button
# use buttons to interact 
# buttons text, image, and compound configuration options as labels
# see the tutorial to 'disable' and change the state of the button
# button states: active, disabled, focus, pressed, selected, background, readonly, alternate, invalid
def myFunctionAction():
    # press button event hanlder
    pass
button = ttk.Button(root, text='Okay', command=myFunctionAction)

# command callback
action = ttk.Button(root, text="Action", default="active", command=myFunctionAction)
root.bind('<Return>', lambda e: action.invoke())

# checkbutton
# checkbutton widget is a button that also holds a binary value
# when checked the checkbutton invokes its callback
# checkbuttons use a value of 1 when checked or 0 when not checked 
# use onvalue and offvalue options to change the defaults
def metricChanged():
    # some action
    pass
measuresSystem = StringVar()
check = ttk.Checkbutton(root, text='Use Metric',
            command=metricChanged, variable=measuresSystem,
            onvalue='metric', offvalue='imperial')
# radiobutton
# a radiobutton widget lets you choose between one of several mutually exclusive choices
# radiobuttons are not limited to just two options (unlike checkbutton)
phone = StringVar()
home = ttk.Radiobutton(root, text='Home', variable=phone, value='home')
office = ttk.Radiobutton(root, text='Office', variable=phone, value='office')
cell = ttk.Radiobutton(root, text='Mobile', variable=phone, value='cell')

# entry
# an entry widget presents users with a single-line text field to type in text
# use width configuration option to provide the number of characters wide for the entry
username = StringVar()
name = ttk.Entry(root, textvariable=username, width=7)
password = StringVar()
passwd = ttk.Entry(root, textvariable=password, show="*")

# Validation - restrict what users can type into the entry
# example: restrict to a zipcode (see the tutorial for a full example)
import re
def check_num(newval):
    return re.match('^[0-9]*$', newval) is not None and len(newval) <= 5
check_num_wrapper = (root.register(check_num), '%P')
num = StringVar()
e = ttk.Entry(root, textvariable=num, validate='key', validatecommand=check_num_wrapper)
e.grid(column=0, row=0, sticky='we')

# combobox
# a combobox widget combines an entry with a list of choices
countryvar = StringVar()
country = ttk.Combobox(root, textvariable=countryvar)
country.bind('<<ComboboxSelected>>', function)
countr['values'] = ('USA','Canada','Australia')





