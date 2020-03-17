background_image_filename = "aiden.jpg"
mouse_image_filename = "logo.png"

import pygame
from pygame.locals import *
from sys import exit

pygame.init()


'''
2 parametro do displat.set_mode

FULLSCREEN
DOUBLEBUF
HWSURFACE
OPENGL
RESIZABLE
NOFRAME

'''

screen = pygame.display.set_mode((640, 480), DOUBLEBUF, 32)
pygame.display.set_caption("HELLO WORLD")

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

'''
.convert() converte a imagem para o mesmo formato do display

'''


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        screen.blit(background, (0,0))
        x, y = pygame.mouse.get_pos()
        x-= mouse_cursor.get_width() / 2
        y-= mouse_cursor.get_height() / 2
        screen.blit(mouse_cursor, (x,y))

        pygame.display.update()
        
        
