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


def generate_numbers(n):
    for i in range(n):
        yield i


generates = generate_numbers(10)
print(generates)
for i in generates:
    print(i)
