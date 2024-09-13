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

movies_container = tk.Listbox(root_container).pack(
    expand=True, fill=tk.BOTH, side=tk.LEFT
)
halls_container = tk.Listbox(root_container).pack(
    expand=True, fill=tk.BOTH, side=tk.LEFT
)
seats_container = tk.Listbox(root_container).pack(
    expand=True, fill=tk.BOTH, side=tk.LEFT
)

root.mainloop()
