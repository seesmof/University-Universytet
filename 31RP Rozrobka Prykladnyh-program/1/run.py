import os 
import json 
import random 
from tkinter import *

GREEN_BUTTON="lawn green"
BLUE_BUTTON="dodger blue"
COLORS=["AntiqueWhite","LightSteelBlue","khaki"]

class Movie:
    def __init__(self, name:str, description:str, year:int, image: str): 
        self.name:str=name
        self.description:str=description
        self.year:int=year
        # посилання на файл зображення
        self.image:str=image
        self.rooms=[
            # генеруємо три зали
            [
                # у кожній залі маємо три ряди сидінь
                [
                    # у кожному ряду маємо сім місць
                    # заповнюємо місця "випадковими" булевими
                    random.choice([0,1]) 
                    for seat in range(7)
                ] 
                for row in range(3)
            ]
            for room in range(3)
        ]

class DataLoader:
    @staticmethod
    def load_movies() -> list[Movie]:
        """
        Завантажує дані про фільми з файлу JSON, конвертує їх до об'єктів типу Movie

        > Список завантажених фільмів як масив об'єктів
        """

        current_folder:str=os.path.dirname(os.path.abspath(__file__))
        movies_data_file_path:str=os.path.join(current_folder,"movies.json")
        movies:list[Movie]=[]

        with open(movies_data_file_path,mode="r",encoding="utf-8") as f: movies_data:dict=json.load(f)
        for movie in movies_data:
            # оскільки ключі прочитаних об'єктів співпадають з полями класу
            # їх можна одразу конвертувати у об'єкти
            movie_object:Movie=Movie(**movie)
            movies.append(movie_object)
        return movies 

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x300")
        self.resizable(0,0)
        self.title("Кінотеатр 'ІСУСОВА Благодать'")
        # при натисканні кнопки Esc програма закривається
        self.bind("<Escape>",lambda _: window.destroy())

window=Window()
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

def place_button(button_object:Button,command):
    button_object.config(command=command)
    button_object.pack(side=LEFT,expand=1,fill=BOTH)

def on_movie_select(movie_index:int):
    global movie
    movie=movies[movie_index]
    build_rooms()

def build_movies():
    movies_container.clear()
    for movie_index,movie in enumerate(movies):
        movie_button=Button(
            movies_container,
            # текст кнопки ставимо на назву фільму
            text=movie.name,
            # обираємо колір за номером фільму
            background=f"{COLORS[movie_index]}1"
        )
        place_button(movie_button,lambda movie_index=movie_index:on_movie_select(movie_index))

def on_room_select(room_index:int):
    global room
    room=movie.rooms[room_index]
    build_seats()

def build_rooms():
    rooms_container.clear()
    for room_index,room in enumerate(movie.rooms):
        room_button=Button(
            rooms_container,
            # текст кнопки ставимо як номер зари
            text=f"Зала {room_index+1}",
            # колір ставимо як номер фільму
            background=f"{COLORS[movies.index(movie)]}1"
        )
        place_button(room_button,lambda room_index=room_index:on_room_select(room_index))

def choose_button_color(value): return GREEN_BUTTON if not value else BLUE_BUTTON

def on_seat_select(row_index,seat_index,button_object):
    global room
    # обираємо протилежне значення до поточного
    room[row_index][seat_index]=0 if room[row_index][seat_index] else 1
    # ставимо колір зелений якщо місце вільне, синій якщо зайняте
    button_object.config(background=choose_button_color(room[row_index][seat_index]))

def build_seats():
    seats_container.clear()
    for row_index, row in enumerate(room): 
        row_container=Container(seats_container,expand=1)
        for seat_index,seat in enumerate(room[row_index]):
            seat_button=Button(row_container,background=choose_button_color(seat))
            place_button(seat_button,lambda row_index=row_index,seat_index=seat_index,button_object=seat_button:on_seat_select(row_index,seat_index,button_object))

movies=DataLoader.load_movies()
build_movies()

if __name__=="__main__": window.mainloop()