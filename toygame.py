
import sys
import math
import pygame
from pygame.locals import *

pygame.init()

mainwindow = pygame.display.set_mode((1280,720))
window_title = pygame.display.set_caption('SUGT08')
#pygame.display.set_icon(G.tl6)
clock = pygame.time.Clock()
pygame.display.flip()

player_w = 25
move_speed = 5
move_up,move_down,move_left,move_right = False,False,False,False

player_location = [100,100]
player_y_momentum = 0

rect_x,rect_y = 300,400
rect_w,rect_h = 200,10

player_rect = pygame.Rect((player_location[0],player_location[1],player_w,player_w),width=0)
test_rect = pygame.Rect((rect_x,rect_y,rect_w,rect_h),width=0)

# 1 rect_x,rect_y 2 rect_x + rect_w,rect_y 3 rect_x,rect_y + rect_h 4 rect_x + rect_w,rect_y + rect_h

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
    pygame.draw.rect(mainwindow,(255,255,255),player_rect)

    player_rect.x = player_location[0] # update rect x
    player_rect.y = player_location[1] # update rect y

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(mainwindow,(255,0,0),test_rect)
        move_up,move_down,move_left,move_right = False,False,False,False
        
        #player_y_momentum = -player_y_momentum
    else:
        pygame.draw.rect(mainwindow,(0,255,0),test_rect)

    '''
    if player_location[1] > 720-50:
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2

    player_location[1] += player_y_momentum
    '''

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

    pygame.display.update()

    clock.tick(60)