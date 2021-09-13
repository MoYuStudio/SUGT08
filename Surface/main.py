
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

keyM = False

alpha = 0

while True:

    mainwindow.fill((255,255,255))

    window_on.set_alpha(alpha)

    window_on.fill((0,0,0))

    surf = pygame.transform.scale(mainwindow, MAINWINDOW_SIZE)

    surf2 = pygame.transform.scale(window_on, WINDOW_SIZE)

    if keyM == True:
        if alpha >= 0 :
            alpha += 10
            window_on.set_alpha(alpha)
        else:
            pass

            

    screen.blit(surf, (0, 0))
    
    screen.blit(surf2, (0, 0))

    pygame.display.update()

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == K_m:
                keyM = True