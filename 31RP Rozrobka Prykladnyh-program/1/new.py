import os

class Movie:
    def __init__(self,name:str):
        self.name=name
        self.rooms=[]
    def generate_rooms(self,count:int=3):
        for c in range(count): self.rooms.append(Room(c))
class Room:
    def __init__(self,number:int=0):
        self.number=number
class DataProcessor:
    def __init__(self):
        self.root=os.path.dirname(os.path.abspath(__file__))
    def get_path(self,file_name:str): return os.path.join(self.root,file_name)