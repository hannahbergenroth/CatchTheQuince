import numpy as np
import pygame, sys, time, random
from pygame.locals import *
from random import randrange

width = 500;
height = 600;

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

basketLeft = 200;
basketTop = 550;
basketwidth = 100;
basketHeight = 30;

speed_x = 0;
 
# initialize screen
pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Catch the Quince')

clock = pygame.time.Clock()
 
# fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)

 
#circle = pygame.draw.circle(background, GREEN , (150,150), 15, 0)
#rectangle = pygame.Rect(basketLeft, basketTop, basketwidth, basketHeight)

crclCentreY = 10
crclCentreX = 250
crclYStepFalling = 10
score = 0
missed = 0
reward = 0
font = pygame.font.Font(None, 30)
 
# display some text
#font = pygame.font.Font(None, 36)
#text = font.render("Hello from Monty PyGame", 1, (10, 10, 10))
#textpos = text.get_rect()
#textpos.centerx = background.get_rect().centerx
#background.blit(text, textpos)
 
# blit everything to the screen
screen.blit(background, (0, 0))
pygame.display.flip()
 
# event loop

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
                
    screen.fill(WHITE)
                
    #s = State(rectangle, Circle(crclCentreX, crclCentreY)
            
        #print(crclCentreX)
        
       
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basketLeft > 0:
        basketLeft -= 50
        print(basketLeft)
    if keys[pygame.K_RIGHT] and basketLeft < width-basketwidth:
        basketLeft += 50
        print(basketLeft)
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
            
    crclCentreY += crclYStepFalling
            
            
    pygame.draw.circle(screen, RED, (crclCentreX, crclCentreY),
                           10)  # circle(Surface, color, pos(x, y), radius, width=0)
        
    if crclCentreY >= basketTop:
        crclCentreY = 10
        crclCentreX = (randrange(10))*55+25
        
    pygame.draw.rect(screen, GREEN, (basketLeft,basketTop,basketwidth,basketHeight))
        
    text = font.render('score: ' + str(score), True, (238, 58, 140))  # update the score on the screen
    text1 = font.render('missed: ' + str(missed), True, (238, 58, 140))  # update the score on the screen
    screen.blit(text, (width - 120, 10))  # render score
    screen.blit(text1, (width - 280, 10))  # render missed
        
    pygame.display.update()
