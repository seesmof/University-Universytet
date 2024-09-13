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

root_container = tk.Frame(root)
root_container.pack(fill=tk.BOTH, expand=True, padx=7, pady=7)


def movie_select(_: tk.Event):
    selected_index = movies_container.curselection()[0]
    movie_name = movies_container.get(selected_index)
    print(
        f"JESUS REIGNS HALLELUJAH JESUS THANK YOU JESUS HALLELUJAH JESUS THANK YOU JESUS HALLELUJAH AMEN: {movie_name}"
    )
    movies_data = {
        "The Passions of the Christ": [1, 2, 3],
        "The Nativity Story": [4, 5, 6],
        "The Questions of Faith": [7, 8, 9],
    }
    halls_container.delete(0, tk.END)
    for hall in movies_data.get(movie_name, []):
        halls_container.insert(tk.END, f"Hall {hall}")


movies_container = tk.Listbox(root_container)
movies_container.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
movies_container.bind("<<ListboxSelect>>", movie_select)
movies_container.insert(tk.END, "Select movie here...")
movies_container.itemconfig(0, fg="gray")
movies = ["The Passions of the Christ", "The Nativity Story", "The Questions of Faith"]
movies_container.insert(tk.END, *movies)

halls_container = tk.Listbox(root_container)
halls_container.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
# halls_container.bind("<<ListboxSelect>>", hall_select)

seats_container = tk.Listbox(root_container)
seats_container.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
# seats_container.bind("<<ListboxSelect>>", seat_select)

root.mainloop()
