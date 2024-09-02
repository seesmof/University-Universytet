""" 
movies grid
for each movie a page with different rooms 
for each room a grid of seats: marked red if busy and green if free
    each seat is a button, when pressed it will add a sit to our ticket somewhere on the right 
once the seats are selected, a user can either buy the ticket or cancel it
in main menu there would be a section with tickets with ability to give up a ticket 

optionally:
add dates for each ticket and status to ticket 
    if current date is later than the ticket, set it as expired
"""


class Animal:
    def sound(self) -> str:
        print("sound of JESUS' Amazing Grace")


class Dove(Animal):
    def sound(self) -> str:
        return "Dove says: 'JESUS is KING'"


class Lion(Animal):
    def sound(self) -> str:
        return "Lion says: 'GOD ALMIGHTY Reigns forever'"


def make_sound(animal: Animal) -> None:
    print(animal.sound())


make_sound(Dove())
make_sound(Lion())
