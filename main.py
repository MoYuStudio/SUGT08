
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

move_speed = 5
move_x,move_y = 100,100
move_up,move_down,move_left,move_right = False,False,False,False

rect_x,rect_y = 300,200

def move_Fn():
    global move_x,move_y,move_up,move_down,move_left,move_right
    if move_up == True:
        move_y -= move_speed
    if move_down == True:
        move_y += move_speed
    if move_left == True:
        move_x -= move_speed
    if move_right == True:
        move_x += move_speed
    return move_x,move_y,move_up,move_down,move_left,move_right

while True:

    move_Fn()

    mainwindow.fill((0,0,0))

    pygame.draw.rect(mainwindow,(255,255,255),(rect_x,rect_y,200,10),width=0)

    pygame.draw.circle(mainwindow,(255,255,255),(move_x,move_y),25)

    pygame.display.update()

    clock.tick(60)

    distance = math.hypot(move_x-rect_x,move_y-rect_y)


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