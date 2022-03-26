import tkinter as tk
from tkinter.tix import COLUMN
from typing import Text
import ctypes
import key_changer
from pyparsing import col

ctypes.windll.shcore.SetProcessDpiAwareness(1)
window = tk.Tk()
window.title('en-th keychanger')
window.minsize(width=600 ,height=300)
window.configure(background="#363940")
input_text  = 0
a= tk.StringVar(window)
a.set("auto")

def cop():
  window.clipboard_clear()
  window.clipboard_append(outputt.get())
  window.update()

def _onKeyRelease(event):
  try:
    ctrl  = (event.state & 0x4) != 0
    if event.keycode==88 and  ctrl and event.keysym.lower() != "x": 
        event.widget.event_generate("<<Cut>>")

    if event.keycode==86 and  ctrl and event.keysym.lower() != "v": 
        event.widget.event_generate("<<Paste>>")

    if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")
  except:
    pass

def set_text(entry,text):
    entry.delete(0,tk.END)
    entry.insert(0,text)
    return

def show_output():
   try:
      inputt = input.get()
      typee = a.get()
      if typee == "auto":
        output = key_changer.auto(inputt,not_know=dont_know.get())
      elif typee == "switch":
        output = key_changer.switch(inputt,not_know=dont_know.get()) 
      elif typee == "th>en":
        output = key_changer.th2en(inputt,not_know=dont_know.get())
      elif typee == "en>th":
        output = key_changer.en2th(inputt,not_know=dont_know.get()) 
      else:
        raise ValueError('type not match')
      window.minsize(width=600, height=300)
      set_text(outputt,output)
      output_label.configure(text=output,foreground="#ffffff",background="#363940",font=('Arial', 12))
   except Exception as e:
    output = 'error'
    print(e)
    window.minsize(width=600, height=150)
    set_text(outputt,e)
    output_label.configure(text=output,foreground="#ff0000",background="#363940",font=('Arial', 16))


title_label = tk.Label(master=window,text='text changer',foreground="#ffffff",background="#363940",font=('Arial', 14))
title_label.grid(row= 1,column=2,padx=100,pady=10)

input = tk.Entry(master=window)
input.grid(row= 2,column=0,columnspan=3)


ok_button = tk.Button(master=window, text='change',command=show_output,foreground="white",background="#353839",font=('Arial', 14))
ok_button.grid(row= 3,column=2,pady=20)

outputt = tk.Entry(master=window,foreground="#ffffff",background="#363940",font=('Arial', 12))
outputt.grid(row= 4,column=0,columnspan=3,rowspan=3)

coppy_button = tk.Button(master=window, text='coppy to clipboard',command=cop,foreground="white",background="#353839",font=('Arial', 10))
coppy_button.grid(row=4 ,column=3)

output_label = tk.Label(master=window,foreground="#ffffff",background="#363940",font=('Arial', 12), wraplengt=400)
output_label.grid(row= 5,column=3,columnspan=3,rowspan=3)

option_menu = tk.OptionMenu(window, a, "auto", "switch", "th>en","en>th")
option_menu.grid(row= 1 ,column=3)

dont_know = tk.Label(master=window,text="replace unknow char with",foreground="#ffffff",background="#363940",font=('Arial', 12))
dont_know.grid(row= 2 ,column=3,pady=5)

dont_know = tk.Entry(master=window,font=('Arial', 12))
dont_know.insert(0,"[?]")
dont_know.grid(row= 3 ,column=3,pady=10)

try:
  window.attributes('-topmost',True)
  window.mainloop()
  window.bind_all("<Key>", _onKeyRelease, "+")
except:
  pass
