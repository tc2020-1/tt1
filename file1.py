from tkinter import *
import webbrowser
root = Tk()
text = Text(root,width = 30,height = 5)
text.pack()
text.insert(INSERT,'I love Fishc.com')
text.tag_add('link',1.7,1.16)
text.tag_config('link',foreground = 'blue',underline = True)

def show_hand_cursor(event):
    text.config(cursor = 'arrow')
def show_arrow_cursor(event):
   text.config(cursor = 'xterm')
def click(event):
    webbrowser.open('http://www.fishc.com')


