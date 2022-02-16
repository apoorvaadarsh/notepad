from tkinter import *
import tkinter as tk;

import linenumber as ln
 
root = Tk()
fram = Frame(root)
 
Label(fram, text ='Find').pack(side = LEFT)
textpad = Entry(fram)
 
textpad.pack(side = LEFT, fill = BOTH, expand = 1)
textpad.focus_set()
 
Find = Button(fram, text ='Find')
Find.pack(side = LEFT)
 
 
Label(fram, text = "Find Exact").pack(side = LEFT)
 
edit2 = Entry(fram)
edit2.pack(side = LEFT, fill = BOTH, expand = 1)
edit2.focus_set()
 
findExactButton = Button(fram, text = 'Find Exact')
findExactButton.pack(side = LEFT)
 
fram.pack(side = TOP)
 
text = Text(root)
 
text.insert('1.0', '''Type your text here''')
text.pack(side = BOTTOM)

#find function
def find():
    s = textpad.get()
    text.tag_remove('found', '1.0', END)

    if (s):
        idx = '1.0'
        while True:
            idx = text.search(s, idx, nocase = True,
                            stopindex = END)
             
            if not idx: break
            lastidx = '% s+% dc' % (idx, len(s))
             
            text.tag_add('found', idx, lastidx)
            idx = lastidx
          
        text.tag_config('found', foreground ='red')
    textpad.focus_set()

#find exacr matching
def findExact():
    s = edit2.get()
    text.tag_remove('found', '1.0', END)

    if (s):
        idx = '1.0'
        while True:
            idx = text.search(s, idx, nocase = False,
                            stopindex = END)
             
            if not idx: break
            lastidx = '% s+% dc' % (idx, len(s))
             
            text.tag_add('found', idx, lastidx)
            idx = lastidx
          
        text.tag_config('found', foreground ='red')
    textpad.focus_set()

 
                 
l = ln.LineNumbers(root, text, width=1)
l.pack(side=tk.RIGHT)
text.pack(side=tk.RIGHT, expand=1)
Find.config(command = find)
findExactButton.config(command = findExact)
root.mainloop()