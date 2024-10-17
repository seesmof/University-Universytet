from abc import abstractmethod

class Transport:
    def __init__(self,name:str):
        self.name=name
    
    @abstractmethod
    def show_kind(self): ...

class Plane(Transport):
    def __init__(self,name:str,kind:str):
        super().__init__(name)
        self.kind:str=kind
    
    def show_kind(self): print(f"Транспорт типу {self.kind}")

plane_object=Plane("Boeing 777","літак")
plane_object.show_kind()