
import sys
import math
import pygame
from pygame.locals import *

pygame.init()

window_title = pygame.display.set_caption('SUGT08')

WINDOW_SIZE = (600,400) # set up window size
TILE_SIZE = 25

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate screen

MAINWINDOW_SIZE = [600,400]
mainwindow = pygame.Surface((MAINWINDOW_SIZE))
#pygame.display.set_icon(G.tl6)
clock = pygame.time.Clock()
pygame.display.flip()

player_w = 20
player_h = 25
move_speed = 5
move_up,move_down,move_left,move_right = False,False,False,False

player_location = [100,100]
player_y_momentum = 0
air_timer = 0


player_rect = pygame.Rect((player_location[0],player_location[1],player_w,player_h),width=0)

def player_display():

    pygame.draw.rect(mainwindow,(255,255,255),(player_location[0],player_location[1],player_w,player_h),width=0)

    # pygame.draw.rect(mainwindow,(255,255,0),(player_location[0],player_location[1],player_w,player_h),width=1)

    # 衣服
    pygame.draw.rect(mainwindow,(255,0,0),(player_location[0],player_location[1]+player_h/2,player_w,player_h/2),width=0)

    # 眼睛
    pygame.draw.rect(mainwindow,(0,0,0),(player_location[0]+player_w/7,player_location[1]+player_h/7,player_w/1.2,player_h/7),width=0)

    # 手 左
    pygame.draw.rect(mainwindow,(255,255,255),(player_location[0]-player_w/4-player_w/7,player_location[1]+player_w/1.5,player_w/3,player_w/3),width=0)
    
    # 手 右
    pygame.draw.rect(mainwindow,(255,255,255),(player_location[0]+player_w+player_w/7,player_location[1]+player_w/1.5,player_w/3,player_w/3),width=0)


def move_Fn():
    global player_location,move_up,move_down,move_left,move_right
    if move_up == True:
        player_location[1] -= move_speed
    if move_down == True:
        player_location[1] += move_speed
    if move_left == True:
        player_location[0] -= move_speed
    if move_right == True:
        player_location[0] += move_speed
    return player_location,move_up,move_down,move_left,move_right

while True:

    move_Fn()

    mainwindow.fill((0,0,0))

    #pygame.draw.circle(mainwindow,(255,255,255),(player_location[0],player_location[1]),player_w)
    player_display()

    surf = pygame.transform.scale(mainwindow, WINDOW_SIZE)
    screen.blit(surf, (0, 0))

    pygame.display.update()

    clock.tick(60)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_w:
                move_up = True
                
            if event.key == K_DOWN or event.key == K_s:
                move_down = True

            if event.key == K_LEFT or event.key == K_a:
                move_left = True

            if event.key == K_RIGHT or event.key == K_d:
                move_right = True
        
        if event.type == KEYUP:
            if event.key == K_UP or event.key == K_w:
                move_up = False
                
            if event.key == K_DOWN or event.key == K_s:
                move_down = False

            if event.key == K_LEFT or event.key == K_a:
                move_left = False

            if event.key == K_RIGHT or event.key == K_d:
                move_right = False

