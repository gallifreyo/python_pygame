background_image_filename = "wallpaper.jpg"
ball_image_filename = "ball.png"
#win_image_filename = "win.png"
#loose_image_filename = "loose.png"

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#tamanho das raquetes
xEntity = 80
yEntity = 20

# definindo o inimigo
enemy = pygame.Rect(300, 5, xEntity, yEntity)

# tamanho da bola
txBall = 15
tyBall = 15

# posicao da bola
ball_x = 320
ball_y = 240

# definindo a bola
ball = pygame.Rect(ball_x, ball_y, txBall, tyBall)

# posicao do player
xPlayer = 200
yPlayer = 455

# definindo o player
Player = pygame.Rect(xPlayer,yPlayer, xEntity, yEntity)

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

font = pygame.font.SysFont("arial", 80)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

pygame.display.set_caption("PONG")

background = pygame.image.load(background_image_filename).convert()

win = "YOU WIN"
#pygame.image.load(win_image_filename).convert_alpha()
loose = "YOU LOOSE"
#pygame.image.load(loose_image_filename).convert_alpha()

text_surface_win = font.render(win, True, (255, 0, 0))

text_surface_loose = font.render(loose, True, (255, 0, 0))

clock = pygame.time.Clock()

RIGHT = False
LEFT = False

my_direction = LEFT

speed = 20

speed_ball_x, speed_ball_y = 8, 8

while True:

    clock.tick(60)
    
    ball.move_ip(speed_ball_x,speed_ball_y)
    
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
        
        #mov enemy
        #enemy.move_ip(+speed,0)

        #mov player
        Player.move_ip(+speed,0)

        
    if LEFT == True:

        
        # mov enemy
        #enemy.move_ip(-speed,0)
        
        # mov player
        Player.move_ip(-speed,0)

    # IA simples enemy

        #while enemy.right != ball.right:
            



        
    # colisao do player -------------------------
    if Player.right >= WINDOW_WIDTH:
        Player.x = 552
    if Player.x < 5:
        Player.x = 5

    # colisao do inimigo ------------------------
    if enemy.right >= WINDOW_WIDTH:
        enemy.x = 552
    if enemy.left < 0:
        enemy.left = 5

    # colisao da bola ---------------------------

    
    if ball.right >= WINDOW_WIDTH:
        speed_ball_x = -speed_ball_x
        #ball.x = 640 - ball_x
        
        # essa merda inverte a posicao para o outro lado da parede
        #ball.right = 640 - ball.x
        
    if ball.left <= 0:
        speed_ball_x = -speed_ball_x
        #ball.x = 0

    if ball.top <= 0:
        #speed_ball_y = -speed_ball_y
        #ball.y = 0
        background.blit(text_surface_win, (140,100))
       

    if ball.bottom >= WINDOW_HEIGHT:
        #speed_ball_y = -speed_ball_y
        #ball.y = 480 - ball_y
        background.blit(text_surface_loose, (120,100))
        
    
    # verificando colisoes de raquetes com a bola

    if Player.colliderect(ball):
        speed_ball_y = -speed_ball_y
    if enemy.colliderect(ball):
        speed_ball_y = -speed_ball_y
        
    

    
    


    screen.blit(background, (0,0))

    pygame.draw.rect(screen, (255,0,0), Player)

    pygame.draw.rect(screen, (255,0,0), enemy)
    pygame.draw.rect(screen, (0,255,0), ball)


    pygame.display.update()
        
        
