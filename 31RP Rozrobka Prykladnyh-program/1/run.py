import os 
import json 
import random 
from tkinter import *

current_folder=os.path.dirname(os.path.abspath(__file__))
movies_data_file_path=os.path.join(current_folder,"movies.json")

class Movie:
    name: str 
    description: str 
    year: int 
    image: str 

    def __init__(self, name:str, description:str, year:int, image: str): 
        self.name=name
        self.description=description
        self.year=year
        self.image=image
        self.rooms=[
            [[random.choice([0,1]) for seat in range(7)] for row in range(3)]
            for room in range(3)
        ]

def show_seats(room):
    for row in room:
        print("".join(["🟢" if not seat else "🔵" for seat in row]))

def load_movies():
    with open(movies_data_file_path,mode="r",encoding="utf-8") as f: movies_data=json.load(f)
    movies:list[Movie]=[]
    for movie in movies_data:
        movie_object=Movie(**movie)
        movies.append(movie_object)
    return movies 

movies=load_movies()

window=Tk()
window.geometry("700x300")
window.resizable(0,0)
window.title("Cinema")
window.config(background="white")
window.bind("<Escape>",lambda _: window.destroy())

room=movies[-1].rooms[-1]
show_seats(room)

rows=[]
for index, row in enumerate(room,start=1): 
    container=Frame(window,bg=f"LightSkyBlue{index}")
    container.pack(side=TOP,fill=BOTH,expand=1)
    rows.append(container)
for index,row in enumerate(rows):
    for seat in room[index]:
        seat_button=Button(row,text=str(seat))
        seat_button.pack(side=LEFT,fill=BOTH,expand=1)

if __name__=="__main__": window.mainloop()