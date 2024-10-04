""" 
fil'my, zaly, miscja

Movie
    id 
    name 
    rooms 
    
Room 
    id 
    number 
    seats

Seat
    id
    row
    number 

Ticket
    id
    movie
    room
    row
    seat


Film 
    nazva 
    zaly 

Zala 
    miscja 

Misce 
    status
    rjad 
    nomer 
"""

import os
import json
import sqlite3

current_dir: str = os.path.dirname(os.path.abspath(__file__))
data_base: str = os.path.join(current_dir, "data.db")

""" 
daily Psalm and Proverb dont join into the general link 
when periscope is selected, section colors dont work 
"""
