import sys

from Tkinter import Button,mainloop
x=Button(text="pm",command=(lambda:sys.stdout.write('12345')))

x.pack()

mainloop()
