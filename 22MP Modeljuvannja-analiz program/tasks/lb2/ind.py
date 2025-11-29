"""
mechanical workshop
from second 0 
each 3 min red parts mass 2kg
each 5 min red parts mass 2.4kg
each 20 min green parts mass 3kg and temperature 85 and two holes
red parts go to drilling machine
there each part has one hole driller in it
red parts take 15 min to drill
green parts go to lathe
at lathe they take 20 min to process
takes 4 minutes to take on and off machine for each part 
model the mechanical workshop working for 8 hours
output queue for drilling machine
"""

workshop = {
    "startingTime": 0,
    "timeToTakeParts": 4,
    "timeToWork": 8 * 60,
    "parts": {
        "red": {"mass": 2, "interval": 3, "holes": 0},
        "heavyRed": {"mass": 2.4, "interval": 5, "holes": 0},
        "green": {"mass": 3, "interval": 20, "temperature": 85, "holes": 2},
    },
    "machines": {
        "drilling machine": {"duration": 15, "parts": ["red", "heavyRed"]},
        "lathe": {"duration": 20, "parts": ["green"]},
    },
}
