""" 
Продаж квитків у кінотеатр з можливістю переглядати фільми, переглядати доступні та зайняті місця для перегляду заданого фільму у відповідній залі, бронювання та звільнення місць.

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
import os
import json
import random
teka=os.path.dirname(os.path.abspath(__file__))

class JsonProcessor:
    def __init__(self, file_name:str):
        self.name=file_name if ".json" in file_name else f"{file_name}.json"
        self.shljah=os.path.join(teka,self.name)
    def read_data(self) -> dict: 
        with open(self.shljah,encoding="utf-8",mode="r") as f: return json.load(f)
    def write_data(self,data:dict):
        with open(self.shljah,encoding="utf-8",mode="w") as f: json.dump(data,indent=2)

""" 
file name data
load file data 
generate rooms 
    3 rooms in total 
    for each room take 3 rows and 7 columns 
    generate "random" True False values for each room
"""

class DataHandler:
    def __init__(self,file_name:str="data"):
        self.data:dict=JsonProcessor(file_name).read_data()
        self.rooms:list[list[bool]]=self.generate_rooms()
    def generate_rooms(self,rooms:int=3):
        def generate_seats(rows:int=3,cols:int=7): return [[random.choice([0,1]) for col in range(cols)] for row in range(rows)]
        return [generate_seats() for room in range(rooms)]

class Window(Tk):
    def __init__(self, window_title:str="Kinoteatr"):
        super().__init__()
        self.configure_window(title=window_title)

    def configure_window(self,title:str,width:int=700,height:int=400):
        self.geometry(f"{width}x{height}")
        self.configure(background="white")
        self.title(title)
        self.resizable(False,False)
        self.bind("<Escape>", lambda _: self.destroy())

class Page(Frame):
    def __init__(self, window:Window):
        super().__init__(master=window, bg="white")
        self.place_page()

    def place_page(self):
        self.pack(fill=BOTH,expand=True)

    def clear_page(self):
        for w in self.winfo_children(): w.destroy()

    def change_color(color:str):
        self.clear_page()
        self.configure(background=color)
        text_label=Label(self,)

window=Window()
current_page=Page(window=window)

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
