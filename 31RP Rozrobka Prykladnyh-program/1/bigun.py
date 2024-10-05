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

class Window(Tk):
    def __init__(self, window_title:str="Kinoteatr"):
        super().__init__()
        self.configure_window(title=window_title)

    def configure_window(self,title:str):
        self.geometry("700x400")
        self.configure(background="white")
        self.title(title)
        self.resizable(False,False)
        self.bind("<Escape>", lambda _: self.destroy())

window=Window()

current_page=Frame(window,background="white")
current_page.pack(fill=BOTH,expand=True)
def change_page_color(color): 
    clear_page()
    current_page.configure(background=color)
    text_label=Label(current_page,text=color.capitalize())
    text_label.pack(anchor=CENTER,expand=True)
def clear_page(): 
    for w in current_page.winfo_children(): w.destroy()

buttons_container=Frame(window)
buttons_container.pack(side=BOTTOM,fill=X)

yellow_button=Button(buttons_container, text="Yellow", command=lambda: change_page_color("yellow"))
yellow_button.pack(side=LEFT, expand=True, fill=X)

blue_button=Button(buttons_container, text="Blue", command=lambda: change_page_color("cyan"))
blue_button.pack(side=LEFT, expand=True, fill=X)

if __name__=="__main__": window.mainloop()
