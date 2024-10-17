import os 
import json 
import random 
from tkinter import *

GREEN_BUTTON="lawn green"
BLUE_BUTTON="dodger blue"
COLORS=["AntiqueWhite","LightSteelBlue","khaki"]

class DataLoader:
    @staticmethod
    def load_movies():
        current_folder=os.path.dirname(os.path.abspath(__file__))
        movies_data_file_path=os.path.join(current_folder,"movies.json")

        with open(movies_data_file_path,mode="r",encoding="utf-8") as f: 
            movies_data=json.load(f)

        movies:list[Movie]=[]
        for movie in movies_data:
            movie_object=Movie(**movie)
            movies.append(movie_object)
        return movies 

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

class Container(Frame):
    def __init__(self,parent,expand:bool=0):
        super().__init__(parent,background="white")
        self.pack(fill=BOTH,expand=expand)

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

movies_container=Container(window)
rooms_container=Container(window)
seats_container=Container(window,expand=1)

def on_movie_select(movie_index:int):
    global movie
    movie=movies[movie_index]
    build_rooms()

def build_movies():
    movies_container.clear()
    for movie_index,movie in enumerate(movies):
        button_object=Button(movies_container,text=movie.name,background=f"{COLORS[movie_index]}1")
        button_object.config(command=lambda movie_index=movie_index:on_movie_select(movie_index))
        button_object.pack(side=LEFT,expand=1,fill=BOTH)

def on_room_select(room_index:int):
    global room
    room=movie.rooms[room_index]
    build_seats()

def build_rooms():
    rooms_container.clear()
    for room_index,room in enumerate(movie.rooms):
        button_object=Button(rooms_container,text=f"Зала {room_index+1}",background=f"{COLORS[movies.index(movie)]}1")
        button_object.config(command=lambda room_index=room_index:on_room_select(room_index))
        button_object.pack(side=LEFT,expand=1,fill=BOTH)

def on_seat_select(row_index,seat_index,button_object):
    global room
    room[row_index][seat_index]=0 if room[row_index][seat_index] else 1
    button_object.config(background=GREEN_BUTTON if not room[row_index][seat_index] else BLUE_BUTTON)

def build_seats():
    seats_container.clear()
    for row_index, row in enumerate(room): 
        row_container=Frame(seats_container,bg=f"LightSkyBlue{row_index+1}")
        row_container.pack(side=TOP,expand=1,fill=BOTH)

        for seat_index,seat in enumerate(room[row_index]):
            seat_button=Button(row_container,background=GREEN_BUTTON if not seat else BLUE_BUTTON)
            seat_button.config(command=lambda row_index=row_index,seat_index=seat_index,button_object=seat_button:on_seat_select(row_index,seat_index,button_object))
            seat_button.pack(side=LEFT,fill=BOTH,expand=1)

movies=DataLoader.load_movies()
build_movies()

if __name__=="__main__": window.mainloop()