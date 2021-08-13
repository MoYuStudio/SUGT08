
import sys
import pygame
from pygame.locals import *

pygame.init()

window_title = pygame.display.set_caption('SUGT08')

WINDOW_SIZE = (600,400)
TILE_SIZE = 32

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate screen

mainwindow = pygame.Surface((600, 400))
#pygame.display.set_icon(G.tl6)
clock = pygame.time.Clock()
pygame.display.flip()