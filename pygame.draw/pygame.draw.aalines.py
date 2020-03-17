import pygame
from pygame.locals import *
from sys import exit
from random import *

pygame.init()

screen = pygame.display.set_mode((640, 480), DOUBLEBUF, 32)

points = []

while True:
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == MOUSEMOTION:
            points.append(event.pos)
            if len(points)>600:
                del points[0]
           
    screen.fill((255,255,255))
    
# se pygame.draw.line tiver como True uma linha sera desenhada enrte o 1 e o ultimo ponto da linha


    if len(points)>1:
        pygame.draw.aalines(screen, (0,255,0), False, points, 2)
           
    pygame.display.update()
