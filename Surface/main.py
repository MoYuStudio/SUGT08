
import sys
import math
import pygame
from pygame.locals import *

pygame.init()

window_title = pygame.display.set_caption('SUGT08')

WINDOW_SIZE = (600,400) # set up window size

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate screen

MAINWINDOW_SIZE = [600,400]
mainwindow = pygame.Surface((MAINWINDOW_SIZE))
WINDOW_SIZE = [100,100]
window_on = pygame.Surface((WINDOW_SIZE))

clock = pygame.time.Clock()
pygame.display.flip()


while True:

    mainwindow.fill((255,255,255))

    window_on.fill((255,0,255))

    surf = pygame.transform.scale(mainwindow, MAINWINDOW_SIZE)
    screen.blit(surf, (0, 0))
    surf2 = pygame.transform.scale(window_on, WINDOW_SIZE)
    screen.blit(surf2, (0, 0))

    pygame.display.update()

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()