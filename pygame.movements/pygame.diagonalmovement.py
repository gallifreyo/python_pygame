import pygame
from pygame.locals import *
from sys import exit



background_image_filename = "cenario.jpg"
sprite_image_filename = "goku.png"

pygame.init()

screen = pygame.display.set_mode((640, 480), DOUBLEBUF, 32)



background = pygame.image.load(background_image_filename).convert()
goku = pygame.image.load(sprite_image_filename).convert_alpha()

goku = pygame.Surface([30,40])

# Objeto clockl

clock = pygame.time.Clock()

x, y = 100, 100

speed_x, speed_y = 133, 170

print("size = ", goku.get_size())

  
while True:
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
           
    screen.blit(background, (0,0))
    screen.blit(goku, (x,y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    x += speed_x * time_passed_seconds
    y += speed_y * time_passed_seconds


    # se o sprite ultrapassar a borda da tela move ele de volta
    
    if x > 640 - goku.get_width():
        speed_x = -speed_x
        x = 640 - goku.get_width()
        
    elif x < 0:
        speed_x = -speed_x
        x = 0

    if y > 480 - goku.get_height():
        speed_y = -speed_y
        y = 480 - goku.get_height()
        
    elif y < 0:
        speed_y = -speed_y
        y = 0
        
           
    pygame.display.update()


 
