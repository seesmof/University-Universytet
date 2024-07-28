import pygame
from pygame.locals import *
import random
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def generateColor():
    colorsPool = [
        "yellow",
        "wheat1",
        "violetred1",
        "violet",
        "turquoise1",
        "tomato",
        "thistle1",
        "steelblue1",
        "springgreen",
        "rosybrown1",
        "seagreen1",
        "powderblue",
        "paleturquoise1",
        "palegreen1",
        "orchid1",
        "olivedrab1",
        "moccasin",
    ]
    return random.choice(colorsPool)


def generateCoordinates(
    screenWidth=800, screenHeight=400, offset=100, maximumRadius=20
):
    return {
        "x": random.randint(offset, screenWidth - maximumRadius),
        "y": random.randint(offset, screenHeight - maximumRadius),
    }


def generateObjects(
    standNumber=random.randint(1, 10), thrownNumber=random.randint(1, 5)
):
    stand = [
        StandObject(
            x=generateCoordinates()["x"],
            y=generateCoordinates()["y"],
            moving=random.randint(0, 1),
        )
        for i in range(standNumber)
    ]
    return stand


class StandObject:
    def __init__(self, x, y, moving):
        self.x = x
        self.y = y
        self.moving = moving
        self.points = random.randint(1, 10)
        self.lastMoved = pygame.time.get_ticks()
        self._radius = random.randint(10, 20)
        self._color = generateColor()

    def draw(self, screen):
        pygame.draw.circle(screen, self._color, (self.x, self.y), self._radius)

    def move(self):
        coordinates = generateCoordinates()
        self.x = coordinates["x"]
        self.y = coordinates["y"]
        self.lastMoved = pygame.time.get_ticks()


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Thrower Game")
clock = pygame.time.Clock()

standObjects = generateObjects()

while True:
    for event in pygame.event.get():
        ESCAPE_KEY_PRESSED = event.type == KEYDOWN and event.key == K_ESCAPE
        if event.type == pygame.QUIT or ESCAPE_KEY_PRESSED:
            exit()
    screen.fill("white")

    for object in standObjects:
        if object.moving:
            if pygame.time.get_ticks() - object.lastMoved >= 3000:
                object.move()
        object.draw(screen)
    pygame.display.flip()
    clock.tick(60)
