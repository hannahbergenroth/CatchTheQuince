import numpy as np
from classes import State, Circle
import pygame, sys, time, random
from definitions import *
from pygame.locals import *
from random import randrange

def main():

    basketLeft = 200;
    basketTop = 550;
    basketwidth = 100;
    basketHeight = 30;
     
    # initialize screen

    pygame.init()
    screen = pygame.display.set_mode((width, height), 0, 32)
    pygame.display.set_caption('Catch the Quince')

    clock = pygame.time.Clock()
     
    # fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((WHITE))
    
    #use image as object
    #quince = pygame.image.load('quince.png')
    #quince = pygame.transform.scale(quince, (50,40))
    #quince_rect = quince.get_rect()

     
    #circle = pygame.draw.circle(background, GREEN , (150,150), 15, 0)
    #rectangle = pygame.Rect(basketLeft, basketTop, basketwidth, basketHeight)

    crclCentreY = 10
    crclCentreX = 250
    crclYStepFalling = 10
    score = 0
    missed = 0
    reward = 0
    font = pygame.font.Font(None, 30)
    rect1 = pygame.Rect(0, 30, 100, 100)
    rect2 = pygame.Rect(basketLeft,basketTop,basketwidth,basketHeight)
    #fruit = Circle(crclCentreX,crclCentreY)  # circle(Surface, color, pos(x, y), radius, wi
    
    #s = State(rect1,Circle(10,10))

     
    # display some text
    #font = pygame.font.Font(None, 36)
    #text = font.render("Hello from Monty PyGame", 1, (10, 10, 10))
    #textpos = text.get_rect()
    #textpos.centerx = background.get_rect().centerx
    #background.blit(text, textpos)
     
    # blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    move_it = False
    move_direction = 1
     
    # event loop

    while True:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print(mouseX)
                if(rect1.collidepoint((mouseX, mouseY))):
                    move_it = not move_it
          
        if move_it:
            rect1.move_ip(0,move_direction * 5)
            if not screen.get_rect().contains(rect1):
                move_direction = move_direction * -1
                rect1.move_ip(0, move_direction * 5)
         
        
        pygame.draw.rect(screen, BLACK, rect1, 1)
        #pygame.draw.rect(screen, (255,255,255, 255), quince_rect, 1)
        pygame.display.flip()
        
                    
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
        
        fruit = pygame.draw.circle(screen, YELLOW, (crclCentreX, crclCentreY), 10)
        # circle(Surface, color, pos(x, y), radius, width=0)
        #fruit.move_ip(move_direction * 5, 0)
        
        #quince_rect.move_ip(0, move_direction * 5)
        #screen.blit(quince, quince_rect)
        
        rect2 = pygame.draw.rect(screen, GREEN, (basketLeft,basketTop,basketwidth,basketHeight), 0)
                
            
        pygame.draw.rect(screen, GREEN, (basketLeft,basketTop,basketwidth,basketHeight))
            
        text = font.render('score: ' + str(score), True, (238, 58, 140))  # update the score on the screen
        text1 = font.render('missed: ' + str(missed), True, (238, 58, 140))  # update the score on the screen
        screen.blit(text, (width - 120, 10))  # render score
        screen.blit(text1, (width - 280, 10))  # render missed
        
        if crclCentreY >= basketTop:
            crclCentreY = 10
            crclCentreX = (randrange(10))*55+25
            if fruit.colliderect(rect2):
                rect2.top=0
                score += 1
              #  fruit = pygame.draw.circle(screen, RED, (crclCentreX, crclCentreY), 10)  # circle(Surface, color, pos(x, y), radius, wi
            elif screen.get_rect().contains(fruit):
                missed += 1
            
        pygame.display.update()
        
if __name__ == '__main__':
    main()
