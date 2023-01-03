from tkinter import *
from tkinter import ttk

# https://tkdocs.com/tutorial/concepts.html

""" Tk concepts
----------------
 Widgets are all the things you see on the screen. Example, button, an entry, labels and frames.
 Widgets are often reffered to as "Controls".
 Widgets are objects, instances of classes, when you want to create a widget,
 you will need to specific class of the widget you'd like to instantiate. 
 To create one you'll need its parent. Widgets are contained within something else, like a window. 
 In Tk, all widgets are part of a widget (or window) hierarchy, with a single root at the top of the hierarchy.

"""

# root = Tk()  # Create instance
# content = ttk.Frame(root)  # Creating a frame
# button = ttk.Button(content) # Button contained in the frame "content"

"""
 In Python each separate widget is a Python object. When instantiating a widget, you must pass its
 parent as a parameter to the widget class. The only exception is the "root" window, the toplevel 
 window containing everything else. That is automatically created when you instantiate Tk.
"""

"""
 All widgets have several configuration options that control how the widget is displayed or how it behaves.
"""

# Silly program to show responding to different events.
root = Tk()
l = ttk.Label(root, text="Starting...")
l.grid()
l.bind("<Enter>", lambda e: l.configure(text="Moved mouse inside"))
l.bind("<Leave>", lambda e: l.configure(text="Moved mouse outside"))
l.bind("<ButtonPress-1>", lambda e: l.configure(text="Clicked left mouse button"))
l.bind("<3>", lambda e: l.configure(text="Clicked right mouse button"))
l.bind("<Double-1>", lambda e: l.configure(text="Double clicked"))
l.bind(
    "<B3-Motion>", lambda e: l.configure(text="right button drag to %d,%d" % (e.x, e.y))
)
root.mainloop()


"""
Geometry Management 
--------------------

Geometry management is how you place widgets on the screen and precisely where they are placed. 
Good geometry management relies on quite sophisticated algorithms. 
Tk's grid is, without a doubt one of the absolute best. 

How it works
------------

Geometry management in Tk relies on the concept of master and slave widgets. A master is a widget, 
typically a toplevel application window or a frame. It contains other widgets, called slaves. 
You can think of a geometry manager taking control of the master widget and deciding how all the 
slave widgets will be displayed within it. 

The use of master and slave will be phased out for parent and child soon: https://core.tcl-lang.org/tips/doc/trunk/tip/581.md

Calling grid the geometry manager will tell what slaves to manage within the master. They will be displayed via the column 
and row options. We can also use columnconfigure and rowconfigure to indicate the columns and rows we'd like to expand if 
extra space is available in the window.
"""

"""
Event Handling
---------------

Tk runs an event loop that receives events from the operating system. 
For example, button presses, keystrokes, mouse movement, window resizing, and so on.

Tk generally will take care of management of the event loop. 
"""
