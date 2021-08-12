
import sys
import pygame
from pygame.locals import *

pygame.init()

mainwindow = pygame.display.set_mode((1280,720))
window_title = pygame.display.set_caption('SUGT08')
#pygame.display.set_icon(G.tl6)
clock = pygame.time.Clock()
pygame.display.flip()




while True:

    mainwindow.fill((0,0,0))

    pygame.display.update()

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()