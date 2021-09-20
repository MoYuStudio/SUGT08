
import pygame

import data.constants as C

import resource.graphics as G

class MenuMain:

    def __init__(self):
        self.MenuMain_surface  = pygame.Surface(C.window_size).convert_alpha()

    def graphics(self):
        self.MenuMain_surface.fill((0,0,0,0))
        self.MenuMain_surface.blit(G.menu_backgroundFin, (0,0))

    def blit(self):
        C.screen.blit(self.MenuMain_surface, (0, 0))