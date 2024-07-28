import pygame
from pygame.locals import *
import random
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def chooseRandomColor():
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


def generateRandomCoordinates(
    screenWidth=800, screenHeight=400, offset=100, maximumRadius=20
):
    return random.randint(offset, screenWidth - maximumRadius), random.randint(
        offset, screenHeight - maximumRadius
    )


def generateObjects(
    standNumber=random.randint(1, 10), thrownNumber=random.randint(1, 5)
):
    stand = [
        StandObject(
            x=generateRandomCoordinates()[0],
            y=generateRandomCoordinates()[1],
            moving=random.randint(0, 1),
        )
        for i in range(standNumber)
    ]
    thrown = [
        ThrownObject(
            speed=random.randint(1, 10),
            accuracy=random.randint(1, 10),
        )
        for i in range(thrownNumber)
    ]
    return {"stand": stand, "thrown": thrown}


class StandObject:
    def __init__(self, x, y, moving):
        self.x = x
        self.y = y
        self.moving = moving
        self.radius = random.randint(10, 20)
        self._color = chooseRandomColor()
        self.points = random.randint(1, 10)
        self.lastMoved = pygame.time.get_ticks()

    def draw(self, screen):
        pygame.draw.circle(screen, self._color, (self.x, self.y), self.radius)

    def move(self):
        coordinates = generateRandomCoordinates()
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.lastMoved = pygame.time.get_ticks()


class ThrownObject:
    def __init__(self, speed, accuracy):
        self.radius = random.randint(10, 20)
        self.x = 0
        self.y = 0
        self.speed = speed
        self.accuracy = accuracy
        self.direction = (0, 0)
        self.thrown = False

    def draw(self, screen):
        pygame.draw.circle(screen, "darkgoldenrod1", (self.x, self.y), self.radius)

    def updateDirection(self, mouseX, mouseY):
        self.direction = (mouseX - self.x, mouseY - self.y)
        self.direction = (
            self.direction[0] / self.accuracy,
            self.direction[1] / self.accuracy,
        )


# TODO add little numbers on each stand to indicate points
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Thrower Game")
    clock = pygame.time.Clock()

    generatedObjects = generateObjects()
    standObjects, thrownObjects = generatedObjects["stand"], generatedObjects["thrown"]

    score = 0
    thrownObjectsLeft = len(thrownObjects)
    scoreText = pygame.font.SysFont("Times New Roman", 24).render(
        f"Score: {score} | Objects left: {thrownObjectsLeft+1}", True, "black"
    )

    while True:
        isEscapeKeyPressed = pygame.key.get_pressed()[pygame.K_ESCAPE]
        for event in pygame.event.get():
            if event.type == pygame.QUIT or isEscapeKeyPressed:
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if thrownObjectsLeft == 0:
                    return
                # TODO update score only on object hit
                mouseX, mouseY = event.pos
                # TODO get latest queue object and set its direction
                projectile = thrownObjects.pop()
                projectile.updateDirection(mouseX, mouseY)
                # TODO update latest queue object to the one behind it
                thrownObjectsLeft = len(thrownObjects)

                scoreText = pygame.font.SysFont("Times New Roman", 24).render(
                    f"Score: {score} | Objects left: {thrownObjectsLeft+1}",
                    True,
                    "black",
                )

        screen.fill("white")
        for standObject in standObjects:
            if standObject.moving:
                if pygame.time.get_ticks() - standObject.lastMoved >= 3000:
                    standObject.move()
            standObject.draw(screen)

        screen.blit(scoreText, (550, 10))
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
