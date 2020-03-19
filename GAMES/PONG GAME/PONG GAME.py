background_image_filename = "wallpaper.jpg"
ball_image_filename = "ball.png"

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

x = 200
y = 455

player_skin = pygame.Surface((80,20))
player_skin.fill((255,0,0))

ball_x = 300
ball_y = 300

screen = pygame.display.set_mode((640, 480), 0, 32)

pygame.display.set_caption("PONG")

background = pygame.image.load(background_image_filename).convert()
ball = pygame.image.load(ball_image_filename).convert_alpha()
ball = pygame.transform.scale(ball, (30,30))

clock = pygame.time.Clock()

RIGHT = False
LEFT = False

my_direction = LEFT

speed = 10
speed_x, speed_y = 13, 17

while True:

    clock.tick(60)

    
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                exit()
                
        if event.type == KEYDOWN:
            
            if event.key == K_RIGHT:
                
                RIGHT = True
                    
            if event.key == K_LEFT:

                LEFT = True
        if event.type == KEYUP:
            
            if event.key == K_RIGHT:
                
                RIGHT = False
                    
            if event.key == K_LEFT:

                LEFT = False


    if RIGHT == True:
        x += speed
    if LEFT == True:
        x -= speed
    
    if x > 552:
        x = 552
    if x < 5:
        x = 5

    ball_x += speed_x
    ball_y += speed_y 

    if ball_x > 640 - ball.get_width():
        speed_x = -speed_x
        ball_x = 640 - ball.get_width()
        
    elif ball_x < 0:
        speed_x = -speed_x
        ball_x = 0

    if ball_y > 550 - ball.get_height():
        speed_y = -speed_y
        ball_y = 480 - ball.get_height()
        
    elif ball_y < 0:
        speed_y = -speed_y
        ball_y = 0


        

    screen.blit(background, (0,0))
    screen.blit(player_skin, (x,y))
    screen.blit(ball, (ball_x,ball_y))



    pygame.display.update()
        
        
