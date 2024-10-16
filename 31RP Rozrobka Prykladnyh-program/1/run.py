import os 
import json 
import random 

current_folder=os.path.dirname(os.path.abspath(__file__))
movies_data_file_path=os.path.join(current_folder,"movies.json")

with open(movies_data_file_path,mode="r",encoding="utf-8") as f: movies_data=json.load(f)

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
        self.room=[[random.choice([0,1]) for seat in range(7)] for row in range(3)]

    def show_seats(self):
        for row in self.room:
            print("".join(["🟢" if not seat else "🔵" for seat in row]))

movies:list[Movie]=[]
for movie in movies_data:
    movie_object=Movie(**movie)
    movies.append(movie_object)
for movie in movies:
    print(movie.name)
    movie.show_seats()
    print()
movies[-3].show_seats()