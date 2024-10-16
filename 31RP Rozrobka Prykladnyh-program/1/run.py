import os 
import json 
import random 
from tkinter import *

current_folder=os.path.dirname(os.path.abspath(__file__))
movies_data_file_path=os.path.join(current_folder,"movies.json")
GREEN_BUTTON="lawn green"
BLUE_BUTTON="dodger blue"

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

movies_container=Frame(window,background="cyan2")
movies_container.pack(fill=BOTH)

def on_movie_select(movie_index:int,movie:Movie):
    print(movie_index,movie.name)

for movie_index,movie in enumerate(movies):
    button_object=Button(movies_container,text=movie.name)
    button_object.config(command=lambda movie_index=movie_index,movie=movie:on_movie_select(movie_index,movie))
    button_object.pack(side=LEFT,expand=1,fill=BOTH)

seats_grid_container=Frame(window,background="OliveDrab2")
seats_grid_container.pack(expand=1,fill=BOTH)

def toggle_seat_status(row_index,seat_index,button_object):
    room[row_index][seat_index]=0 if room[row_index][seat_index] else 1
    button_object.config(background=GREEN_BUTTON if not room[row_index][seat_index] else BLUE_BUTTON)

def build_seats_grid(room):
    rows=[]
    for index, row in enumerate(room): 
        container=Frame(seats_grid_container,bg=f"LightSkyBlue{index+1}")
        container.pack(side=TOP,fill=BOTH,expand=1)
        rows.append(container)

    for row_index,row in enumerate(rows):
        for seat_index,seat in enumerate(room[row_index]):
            seat_button=Button(row,background=GREEN_BUTTON if not seat else BLUE_BUTTON)
            seat_button.config(command=lambda row_index=row_index,seat_index=seat_index,button_object=seat_button:toggle_seat_status(row_index,seat_index,button_object))
            seat_button.pack(side=LEFT,fill=BOTH,expand=1)

if __name__=="__main__": window.mainloop()