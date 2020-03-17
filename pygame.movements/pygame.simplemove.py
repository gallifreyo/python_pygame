import pygame
from pygame.locals import *
from sys import exit



background_image_filename = "cenario.jpg"
sprite_image_filename = "goku.png"

pygame.init()

screen = pygame.display.set_mode((640, 480), DOUBLEBUF, 32)

background = pygame.image.load(background_image_filename).convert()
goku = pygame.image.load(sprite_image_filename)

# A cordenada x de nosso sprite (goku)

x = 0

while True:
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
           
    screen.blit(background, (0,0))
    screen.blit(goku, (x,10))
    x += 1

    # se a imagem ultrapassar a extremidade da tela, mova-a de volta
    if x > 640:
        x -= 640
           
    pygame.display.update()

