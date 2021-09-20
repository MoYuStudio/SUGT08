
import sys
import pygame
from pygame.locals import *

import data.constants as C

import resource.graphics as G

import window

class MainGame:

    def __init__(self): 

        pygame.init()
        pygame.mixer.init()

        C.screen = pygame.display.set_mode((C.WINDOW_SIZE),pygame.RESIZABLE)

        self.clock = pygame.time.Clock()

        pygame.display.set_caption(C.window_title)
        pygame.display.set_icon(G.tl6)
        pygame.display.flip()

        self.menu_main = window.MenuMain.MenuMain()

    def gameloop(self): 

        while True:

            C.screen.fill((0,0,0,0))

            self.menu_main.graphics()

            self.menu_main.blit()

            pygame.display.update()

            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit()
                    sys.exit()

            self.clock.tick(C.window_fps)

if __name__ == "__main__":

    main_game = MainGame()
    main_game.gameloop()