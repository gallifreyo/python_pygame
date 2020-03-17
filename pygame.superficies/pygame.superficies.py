background_image_filename = "aiden.jpg"
mouse_image_filename = "logo.png"

import pygame
from pygame.locals import *
from sys import exit

pygame.init()


'''
 




'''

screen = pygame.display.set_mode((640, 480), DOUBLEBUF, 32)

#pygame.display.set_caption("HELLO WORLD")

#background = pygame.image.load(background_image_filename).convert()
blank_surface = pygame.Surface((256, 256))



'''
.convert() converte a imagem para o mesmo formato do display

'''


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        screen.blit(blank_surface, (0,0))

        pygame.display.update()
        
        

