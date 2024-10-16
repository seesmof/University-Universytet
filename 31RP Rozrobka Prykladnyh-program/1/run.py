import os 
import json 
import random 
from tkinter import *

current_folder=os.path.dirname(os.path.abspath(__file__))
movies_data_file_path=os.path.join(current_folder,"movies.json")
GREEN_BUTTON="lawn green"
BLUE_BUTTON="dodger blue"
COLORS=["AntiqueWhite","PaleGreen","khaki"]

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

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x300")
        self.resizable(0,0)
        self.title("Кінотеатр 'ІСУСОВА Благодать'")
        self.bind("<Escape>",lambda _: window.destroy())

window=Window()
movies=None
movie=None
room=None

def clear_container(container:Frame):
    for widget in container.winfo_children():
        widget.destroy()

movies_container=Frame(window,background="white")
movies_container.pack(fill=BOTH)

rooms_container=Frame(window,background="white")
rooms_container.pack(fill=BOTH)

seats_container=Frame(window,background="white")
seats_container.pack(expand=1,fill=BOTH)

def on_movie_select(movie_index:int):
    global movie
    movie=movies[movie_index]
    build_rooms()

def build_movies():
    clear_container(movies_container)
    for movie_index,movie in enumerate(movies):
        button_object=Button(movies_container,text=movie.name,background=f"{COLORS[movie_index]}1")
        button_object.config(command=lambda movie_index=movie_index:on_movie_select(movie_index))
        button_object.pack(side=LEFT,expand=1,fill=BOTH)

def on_room_select(room_index:int):
    global room
    room=movie.rooms[room_index]
    build_seats()

def build_rooms():
    clear_container(rooms_container)
    for room_index,room in enumerate(movie.rooms):
        button_object=Button(rooms_container,text=f"Зала {room_index+1}")
        button_object.config(command=lambda room_index=room_index:on_room_select(room_index))
        button_object.pack(side=LEFT,expand=1,fill=BOTH)

def on_seat_select(row_index,seat_index,button_object):
    global room
    room[row_index][seat_index]=0 if room[row_index][seat_index] else 1
    button_object.config(background=GREEN_BUTTON if not room[row_index][seat_index] else BLUE_BUTTON)

def build_seats():
    clear_container(seats_container)
    for row_index, row in enumerate(room): 
        row_container=Frame(seats_container,bg=f"LightSkyBlue{row_index+1}")
        row_container.pack(side=TOP,expand=1,fill=BOTH)

        for seat_index,seat in enumerate(room[row_index]):
            seat_button=Button(row_container,background=GREEN_BUTTON if not seat else BLUE_BUTTON)
            seat_button.config(command=lambda row_index=row_index,seat_index=seat_index,button_object=seat_button:on_seat_select(row_index,seat_index,button_object))
            seat_button.pack(side=LEFT,fill=BOTH,expand=1)

movies=load_movies()
build_movies()

if __name__=="__main__": window.mainloop()