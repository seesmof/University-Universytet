""" 
sale of tickets to the cinema with the ability to view the sessions, free and occupied seats for each session in the respective hall, reservation and release of seats

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

import tkinter as tk

root = tk.Tk()
root.geometry("700x300")
root.title("JESUS' Cinema")

root_container = tk.Frame(root)
root_container.pack(fill=tk.BOTH, expand=True, padx=7, pady=7)


def movie_select(_: tk.Event):
    try:
        selected_index = movies_container.curselection()[0]
    except IndexError:
        return

    movie_name = movies_container.get(selected_index)

    print(
        f"JESUS REIGNS HALLELUJAH JESUS THANK YOU JESUS HALLELUJAH JESUS THANK YOU JESUS HALLELUJAH AMEN: {movie_name}"
    )


def hall_select(_: tk.Event):
    try:
        selected_index = halls_container.curselection()[0]
    except IndexError:
        return

    hall_name = halls_container.get(selected_index)

    print("JESUS THANK YOU JESUS HALLELUJAH: hall select")


def seat_select(_: tk.Event):
    try:
        selected_index = seats_container.curselection()[0]
    except IndexError:
        return

    seat_name = seats_container.get(selected_index)

    print("JESUS THANK YOU JESUS HALLELUAJH: seat select")


movies_container = tk.Listbox(root_container)
movies_container.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
movies_container.bind("<<ListboxSelect>>", movie_select)
movies = ["The Passions of the Christ", "The Nativity Story", "The Questions of Faith"]
movies_container.insert(tk.END, *movies)

halls_container = tk.Listbox(root_container)
halls_container.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
halls_container.bind("<<ListboxSelect>>", hall_select)

seats_container = tk.Listbox(root_container)
seats_container.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
seats_container.bind("<<ListboxSelect>>", seat_select)

root.mainloop()
