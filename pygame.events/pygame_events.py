import pygame
from pygame.locals import *
from sys import exit


background_image_filename = "aiden.jpg"


pygame.init()


SCREEN_SIZE = (800,600)


screen = pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF
                                 , 32)

background = pygame.image.load(background_image_filename).convert()

x, y = 0, 0

move_x, move_y = 0, 0

while True:
    
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            
            if event.key == K_LEFT:
                move_x = -1
                
            if event.key == K_RIGHT:
                move_x = +1

            elif event.key == K_UP:
                move_y = -1

            elif event.key == K_DOWN:
                move_y = +1

        elif event.type == KEYUP:
            
            if event.key == K_LEFT:
                move_x = 0

            elif event.key == K_RIGHT:
                move_x = 0

            elif event.key == K_UP:
                move_y = 0

            elif event.key == K_DOWN:
                move_y = 0

    x+= move_x
    y+= move_y

    screen.fill((0, 0, 0))
    screen.blit(background, (x, y))

    pygame.display.update()



'''

se tiver usando um display com buffer duplo chame pygame.dsplay.flip()
ao inves de update isso fara a mudanca instantanea do display ao inves de efetuar uma copia dos dados da tela



'''







    
