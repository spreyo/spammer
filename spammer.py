import tkinter.font as tkFont
import ttkthemes
from tkinter import ttk as tk
from ttkthemes import ThemedTk
import tkinter as tktk
import keyboard 
from time import sleep
import urllib3
import urllib.request
from tkinter import messagebox
from pathlib import Path



def stateRequest():
    page = urllib.request.urlopen('https://spreyo-python.000webhostapp.com/')
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    title_index = html.find('<p>')
    start_index = title_index + len("<p>")
    end_index = html.find("</p>")
    global title
    title = html[start_index:end_index]

OUTPUT_PATH = Path(__file__).parent
ICON_PATH = OUTPUT_PATH / Path("./icon.png")


root = ThemedTk(theme='arc',background='gray')
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
root.title('spammer')
# root.iconphoto(True, tktk.PhotoImage(file = ICON_PATH))
# but = tk.Button(root,text='Confirm (F6)')
# but.place(x=240,y=250,width=97,height=38)
spam = False

def TurnOn():
    global spam
    spam = True

def TurnOff():
    global spam
    spam = False

#variables
entry = tktk.StringVar(root)
entryREAD = entry.get()
count = tktk.IntVar(root)

GLabel_923=tktk.Label(root)
ft = tkFont.Font(family='Times',size=16)
GLabel_923["font"] = ft
GLabel_923["fg"] = "#333333"
GLabel_923["justify"] = "center"
GLabel_923["text"] = "What do you want to spam?"
GLabel_923.place(x=170,y=100,width=240,height=70)

GLineEdit_971=tk.Entry(root, textvariable=entry)
ft = tkFont.Font(family='Times',size=10)
GLineEdit_971["font"] = ft
GLineEdit_971["justify"] = "center"
GLineEdit_971.place(x=180,y=180,width=213,height=40)


but = tk.Button(root,text='Confirm (F6)')
but.bind('<Button-1>', lambda x:[TurnOff(), startSpamming()])
but.place(x=240,y=250,width=97,height=38)

GCheckBox_410=tk.Checkbutton(root)
ft = tkFont.Font(family='Times',size=10)
# GCheckBox_410['justify'] = "center"
GCheckBox_410["text"] = "Slow Mode"
GCheckBox_410.place(x=340,y=240,width=110,height=56)
GCheckBox_410["offvalue"] = "0"
GCheckBox_410["onvalue"] = "1"
GCheckBox_410.state(['!selected'])

GLineEdit_40=tk.Entry(root, textvariable=count)
GLineEdit_40["cursor"] = "arrow"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_40["justify"] = "center"
GLineEdit_40.place(x=250,y=300,width=70,height=25)

GLabel_875=tktk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_875["text"] = "Count"
GLabel_875.place(x=250,y=340,width=70,height=25)



#functions
def startSpamming():
    stateRequest()
    print(spam)
    i = 1
    slow = GCheckBox_410.instate(['selected'])
    countValue = count.get()
    print(title)
    if int(title) == 1:
        root.title('spammer')
        while i <= countValue:
            entryREAD = entry.get()
            # keyboard.send('t')
            keyboard.write(entryREAD)
            keyboard.send('enter')
            print(entryREAD)
            print(i)
            i = i + 1
            if slow == True:
                sleep(0.1)
            else: 
                continue

    else:
         messagebox.showerror("Error when trying to connect to the server", "The spammer is currently turned off, please contact @spreyo if you have any problems.")
         root.title('spammer(not connected to server)')
keyboard.add_hotkey('F6', lambda:[TurnOn(), startSpamming()])
keyboard.add_hotkey('F7', lambda:[TurnOff(), startSpamming()])
root.mainloop()