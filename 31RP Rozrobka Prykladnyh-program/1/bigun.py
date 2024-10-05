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
    return root

window=configure_window()

movies_list=Listbox(window)
movies_list.pack(padx=3,pady=3,expand=True,fill=BOTH,side=LEFT)
movies=["Christ","Jesus","King of Kings","Bible","Cross","Sins","Atonement","Election","Grace","Love","Peace","Joy","Trust","Hope","Heaven"]
for movie in movies: movies_list.insert(END,movie)

rooms_list=Listbox(window)
rooms_list.pack(padx=3,pady=3,expand=True,fill=BOTH,side=LEFT)

seats_list=Listbox(window)
seats_list.pack(padx=3,pady=3,expand=True,fill=BOTH,side=LEFT)

if __name__=="__main__": window.mainloop()
