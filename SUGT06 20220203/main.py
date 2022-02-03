
################################################################
#                  MoYu Studio © 2021 -2022                    #
################################################################
#                          Tinyland                            #
#                       SUGT12 a1 Bata                         #
################################################################
#                         MoYu Engine                          #
#                        Powed by SDL2                         #
#              Pygame & Pyglet & Arcade & PyMunk               #
################################################################

# import

import os
import sys

import pygame
from pygame.locals import *

# init

pygame.init()
pygame.display.init()
pygame.mixer.init()

# config

WINDOW_TITLE = 'Tinyland'
WINDOW_SIZE = (1280, 720)
WINDOW_FPS = 60

COLOR_DEFAULT = (255,55,55,0)

ASSETS_PATH = os.getcwd() + os.sep + 'assets' + os.sep

assets = {}

class Assets:
    def __init__(self):
        self.assets = assets

        self.tile_land = {
            'path': ASSETS_PATH + 'tile_land' + os.sep,

            '0':{
                'name':'tileland_air',
                'visibility': False,
                'effect': None,
            },

            '1':{
                'name':'tileland_dirt',
                'visibility': True,
                'effect': None,
            },

            '2':{
                'name':'tileland_grass',
                'visibility': True,
                'effect': None,
            },

        }

        self.background = {
            'path': ASSETS_PATH + 'background' + os.sep,

            '0':{
                'name':'background0',
                'visibility': True,
            },
        }


    def image_load(self):

        self.assets['tile_land'] = {}
        self.assets['background'] = {}
        
        for id in range(0,2+1,1):
            print(self.tile_land['path'] + self.tile_land[str(id)]['name'] + '.png')
            self.assets['tile_land'][id] = pygame.image.load(self.tile_land['path'] + self.tile_land[str(id)]['name'] + '.png').convert_alpha()
        for id in range(0,0+1,1):
            print(self.background['path'] + self.background[str(id)]['name'] + '.png')
            self.assets['background'][id] = pygame.image.load(self.background['path'] + self.background[str(id)]['name'] + '.png').convert_alpha()

        return self.assets

    

class Tilemap:
    def __init__(self):
        pass

    def set(self):
        pass

class Event:
    def __init__(self):
        self.config = {
                            'mouse_motion_pos':[-1,-1],
                            'mouse_click_pos':[-1,-1],
                            'move':[0,0],
                            'zoom':0,
                            'move_speed':10,

                            'move_switch':{
                                            'up':False,
                                            'down':False,
                                            'left':False,
                                            'right':False,
                            },
                            'zoom_switch':{
                                            'in':False,
                                            'out':False,
                            },
                        }

    def set(self):
        for self.event in pygame.event.get():
            
            if self.event.type == QUIT:
                pygame.quit()
                sys.exit()

            if self.event.type == pygame.MOUSEMOTION:
                self.config['mouse_motion_pos'] = self.event.pos

            if self.event.type == pygame.MOUSEBUTTONDOWN:
                self.config['mouse_click_pos'] = self.event.pos

            if self.event.type == pygame.MOUSEBUTTONUP:
                self.config['mouse_click_pos'] = [-1,-1]

            if self.event.type == pygame.KEYDOWN:
                self.move_keydown()
                
            if self.event.type == pygame.KEYUP:
                self.move_keyup()

        return self.config

    def blit(self):
        self.move()
        self.zoom()

    def move(self):
        if self.config['move_switch']['up'] == True:
            self.config['move'][1] -= self.config['move_speed']
        if self.config['move_switch']['down'] == True:
            self.config['move'][1] += self.config['move_speed']
        if self.config['move_switch']['left'] == True:
            self.config['move'][0] -= self.config['move_speed']
        if self.config['move_switch']['right'] == True:
            self.config['move'][0] += self.config['move_speed']

    def move_keydown(self):
        if self.event.key == K_UP or self.event.key == K_w:
            self.config['move_switch']['up']   = True
            
        if self.event.key == K_DOWN or self.event.key == K_s:
            self.config['move_switch']['down'] = True

        if self.event.key == K_LEFT or self.event.key == K_a:
            self.config['move_switch']['left'] = True

        if self.event.key == K_RIGHT or self.event.key == K_d:
            self.config['move_switch']['right'] = True

        return self.config

    def move_keyup(self):
        if self.event.key == K_UP or self.event.key == K_w:
            self.config['move_switch']['up']   = False

        if self.event.key == K_DOWN or self.event.key == K_s:
            self.config['move_switch']['down'] = False

        if self.event.key == K_LEFT or self.event.key == K_a:
            self.config['move_switch']['left'] = False

        if self.event.key == K_RIGHT or self.event.key == K_d:
            self.config['move_switch']['right'] = False

    def zoom(self):
        if self.config['zoom_switch']['in'] == True:
            if self.config['surface_level'] <= 0.25:
                self.config['surface_level'] = 0.25
            else:
                self.config['surface_level'] -= 0.025
                self.config['move'][1] -= 4.25
                self.config['move'][0] -= 7.9
        if self.config['zoom_switch']['out'] == True:
            if self.config['surface_level'] >= 1:
                self.config['surface_level'] = 1
            else:
                self.config['surface_level'] += 0.025
                self.config['move'][1] += 4.25
                self.config['move'][0] += 7.9

    def zoom_keydown(self):
        if self.event.key == K_q:
            self.config['zoom_switch']['in']   = True

        if self.event.key == K_e:
            self.config['zoom_switch']['out']  = True

    def zoom_keyup(self):
        if self.event.key == K_q:
            self.config['zoom_switch']['in']   = False

        if self.event.key == K_e:
            self.config['zoom_switch']['out'] = False


# mainloop

class Mainloop:
    def __init__(self):
        pass

    def run(self):
        # init
        pygame.display.set_caption(WINDOW_TITLE)
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.running = True

        pygame.display.flip()

        assets_manage = Assets()
        assets_manage.image_load()

        # main loop
        while self.running:
            # events
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

            # update

            # draw
            self.screen.fill(COLOR_DEFAULT)

            self.screen.blit(assets['background'][0], (0,0))

            self.screen.blit(assets['tile_land'][1], (WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2))

            pygame.display.update()

            # fps
            self.clock.tick(WINDOW_FPS)


if __name__ == "__main__":

    



    main = Mainloop()
    main.run()