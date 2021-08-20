
import sys
import pygame
from pygame.locals import *

mainwindow = pygame.display.set_mode((600,600))
window_title = pygame.display.set_caption('test')
#pygame.display.set_icon(.icon)
clock = pygame.time.Clock()
pygame.display.flip()

line_color = [255, 255, 255]
line_pos = [180, 100]
line_size = [10, 350]

button_color = [161, 136, 127]
button_pos = [172, 100]
button_size = [25, 50]

moveable = False
move = 0

mouse_x, mouse_y = 0,0
mouse_pos_x,mouse_pos_y = 0,0

while True:

    if move <= 0:
        move = 0
    if move >= 350-button_size[1]:
        move = 350-button_size[1]

    mainwindow.fill((0,0,0))

    pygame.draw.rect(mainwindow, line_color,(line_pos,line_size), width=0)
    pygame.draw.rect(mainwindow, button_color,(button_pos[0],button_pos[1]+move,button_size[0],button_size[1]), width=0)
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:

            mouse_pos_x,mouse_pos_y = event.pos
            if moveable == True:
                move = mouse_pos_y - mouse_y

        if event.type == pygame.MOUSEBUTTONDOWN:

            #print (event.button)

            mouse_x, mouse_y = event.pos

            if button_pos[0] <= mouse_x <= button_pos[0] + button_size[0] and button_pos[1]+move <= mouse_y <= button_pos[1]+move + button_size[1]:
                print('button be clicked')
                moveable = True
            else:
                moveable = False

        if event.type == pygame.MOUSEBUTTONUP:

            moveable = False

        if event.type == MOUSEWHEEL:
            #print(event)
            #print(event.x, event.y)
            #print(event.flipped)
            #print(event.which)

            mousewheel = event.y

            move += mousewheel

            #print(event.y)
