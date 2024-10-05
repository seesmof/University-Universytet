""" 
fil'my, zaly, miscja

Film 
    nazva 
    zaly 

Zala 
    miscja 

Misce 
    status
    rjad 
    nomer 
"""

from tkinter import *

def configure_window():
    root=Tk()
    root.geometry("700x400")
    root.configure(background="white")
    root.title("Kinoteatr")
    root.resizable(False,False)
    root.bind("<Escape>", lambda _: root.destroy())
    return root

window=configure_window()

current_page=Frame(window,background="yellow")
current_page.pack(fill=BOTH,expand=True)
def change_color(color): current_page.configure(background=color)

buttons_container=Frame(window)
buttons_container.pack(side=BOTTOM,fill=X)

green_button=Button(buttons_container, text="Green", command=lambda: change_color("green"))
green_button.pack(side=LEFT, expand=True, fill=X)

blue_button=Button(buttons_container, text="Blue", command=lambda: change_color("blue"))
blue_button.pack(side=LEFT, expand=True, fill=X)

if __name__=="__main__": window.mainloop()
