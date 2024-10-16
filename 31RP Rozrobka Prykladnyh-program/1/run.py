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

movies:list[Movie]=[]
for movie in movies_data:
    movie_object=Movie(**movie)
    movies.append(movie_object)

room=[
   [random.choice([0,1]) for _ in range(7)] 
   for row in range(3)
]
for row in room: 
    print("".join(["🟢" if not seat else "🔵" for seat in row]))