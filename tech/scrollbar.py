
import sys
import pygame
from pygame.locals import *

mainwindow = pygame.display.set_mode((600,600))
window_title = pygame.display.set_caption('test')
#pygame.display.set_icon(.icon)
clock = pygame.time.Clock()
pygame.display.flip()

scrollbar_line_color = [255, 255, 255]
scrollbar_line_pos = [180, 100]
scrollbar_line_size = [10, 350]

scrollbar_button_color = [161, 136, 127]
scrollbar_button_pos = [172, 100]
scrollbar_button_size = [25, 50]

scrollbar_moveable = False
scrollbar_move = 0

mouse_x, mouse_y = 0,0
mouse_pos_x,mouse_pos_y = 0,0

def scrollbar_h_surface():

    global scrollbar_move,scrollbar_line_size,scrollbar_button_size

    if scrollbar_move <= 0:
        scrollbar_move = 0
    if scrollbar_move >= scrollbar_line_size[1]-scrollbar_button_size[1]:
        scrollbar_move = scrollbar_line_size[1]-scrollbar_button_size[1]

    mainwindow.fill((0,0,0))

    pygame.draw.rect(mainwindow, scrollbar_line_color,(scrollbar_line_pos,scrollbar_line_size), width=0)
    pygame.draw.rect(mainwindow, scrollbar_button_color,(scrollbar_button_pos[0],scrollbar_button_pos[1]+scrollbar_move,scrollbar_button_size[0],scrollbar_button_size[1]), width=0)
    
    pygame.display.update()

    return scrollbar_move,scrollbar_line_size,scrollbar_button_size

while True:

    scrollbar_h_surface()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        

        if event.type == pygame.MOUSEMOTION:

            mouse_pos_x,mouse_pos_y = event.pos
            if scrollbar_moveable == True:
                scrollbar_move = mouse_pos_y - mouse_y

        

        if event.type == pygame.MOUSEBUTTONDOWN:

            #print (event.button)

            mouse_x, mouse_y = event.pos
            

            if scrollbar_button_pos[0] <= mouse_x <= scrollbar_button_pos[0] + scrollbar_button_size[0] and scrollbar_button_pos[1]+scrollbar_move <= mouse_y <= scrollbar_button_pos[1]+scrollbar_move + scrollbar_button_size[1]:
                print('button be clicked')
                scrollbar_moveable = True
            else:
                scrollbar_moveable = False

        if event.type == pygame.MOUSEBUTTONUP:

            scrollbar_moveable = False

        if event.type == MOUSEWHEEL:
            #print(event)
            #print(event.x, event.y)
            #print(event.flipped)
            #print(event.which)

            mousewheel = event.y

            scrollbar_move += mousewheel

            #print(event.y)
