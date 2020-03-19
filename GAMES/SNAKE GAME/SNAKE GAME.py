background_image_filename = "wallpaper.jpg"

import pygame
import random
import tkinter
from tkinter import messagebox
from pygame.locals import *
from sys import exit

pygame.init()



def appleOnGrid():
    x = random.randint(0, 639)
    y = random.randint(0, 479)
    return (x//10 * 10, y//10 * 10)

def isColliding(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

root = tkinter.Tk()
root.withdraw()



apple_pos = appleOnGrid()
apple = pygame.Surface((10,10))
apple.fill((0,0,255))



snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,0,0))



UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

my_direction = LEFT


screen = pygame.display.set_mode((640, 480), 0, 32)

pygame.display.set_caption("SNAKE")

background = pygame.image.load(background_image_filename).convert()

clock = pygame.time.Clock()

while True:
    

    clock.tick(25)

    
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                exit()
                
        if event.type == KEYDOWN:
                
            if event.key == K_UP:
                    my_direction = UP
                    
            if event.key == K_DOWN:
                    my_direction = DOWN
                    
            if event.key == K_RIGHT:
                    my_direction = RIGHT
                    
            if event.key == K_LEFT:
                    my_direction = LEFT




    if isColliding(snake[0], apple_pos):
        
        apple_pos = appleOnGrid()
        snake.append((0,0)) 

    if my_direction == UP:
            snake[0] = (snake[0][0] , snake[0][1] - 10)# y sobe (subtrai do eixo y)
            
    if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)# y desce
            
    if my_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1]) # x vai para direita
            
    if my_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1]) # x vai para a esquerda


    for i in range(len(snake)-1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])


    # ao colidir com as paredes posso fazer a cobra quicar ou posso fazer um game over
        
    # eixo x            
    if snake[0][0] > 640:


        my_direction = LEFT
        '''
        if tkinter.messagebox.askyesno(title="GAME OVER", message="retry ?")== True:
            print("recomecando")
        else:
            pygame.quit()
            exit()
            
        '''
        
    if snake[0][0] < 0:

        my_direction = RIGHT
        '''
        if tkinter.messagebox.askyesno(title="GAME OVER", message="retry ?")== True:
            print("recomecando")
        else:
            pygame.quit()
            exit()
        '''
    # eixo y
    if snake[0][1] > 480:

        my_direction = UP
        '''
        if tkinter.messagebox.askyesno(title="GAME OVER", message="retry ?")== True:
            print("recomecando")
        else:
            pygame.quit()
            exit()
        '''
       
        
    if snake[0][1] < 0:

        my_direction = DOWN

        '''
        if tkinter.messagebox.askyesno(title="GAME OVER", message="retry ?")== True:
            print("recomecando")
        else:
            pygame.quit()
            exit()
        '''
        
    
  
    screen.blit(background, (0,0))
    screen.blit(apple, (apple_pos))

    for pos in snake:
        screen.blit(snake_skin, pos)


            

    pygame.display.update()
        
        
