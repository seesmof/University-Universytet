import math
import pygame
from pygame.locals import *
import random
from rich.console import Console
from rich.traceback import install

install()
console = Console()


def generateBalls():
    balls = [
        Ball(x=10, y=10, speed=random.randint(1, 10))
        for i in range(random.randint(1, 5))
    ]
    return balls


class Ball:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = None
        self.accuracy = random.randint(7, 11)

    def draw(self, screen):
        pygame.draw.circle(screen, "darkgoldenrod1", (self.x, self.y), 7)

    def throw(self, target):
        if not self.direction:
            dx, dy = target[0] - self.x, target[1] - self.y
            distance = (dx**2 + dy**2) ** 0.5
            self.direction = (dx / distance, dy / distance)
            distortion = (11 - self.accuracy) / 10
            randomAngle = (random.random() * 2 - 1) * distortion
            self.direction = (
                self.direction[0] * math.cos(randomAngle)
                - self.direction[1] * math.sin(randomAngle),
                self.direction[0] * math.sin(randomAngle)
                + self.direction[1] * math.cos(randomAngle),
            )

    def update(self):
        if self.direction:
            self.x += self.direction[0] * self.speed
            self.y += self.direction[1] * self.speed


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Thrower Game")
clock = pygame.time.Clock()

balls = generateBalls()
thrownBalls = []

while True:
    for event in pygame.event.get():
        ESCAPE_KEY_PRESSED = event.type == KEYDOWN and event.key == K_ESCAPE
        if event.type == pygame.QUIT or ESCAPE_KEY_PRESSED:
            exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            if balls:
                targetBall = balls.pop()
                targetBall.throw(pygame.mouse.get_pos())
                thrownBalls.append(targetBall)
    screen.fill("white")

    for ball in balls:
        ball.draw(screen)
    for ball in thrownBalls:
        ball.update()
        ball.draw(screen)
    pygame.display.flip()
    clock.tick(60)
