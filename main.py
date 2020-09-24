from classes import State, Circle
import pygame, sys, time, random
from definitions import *
from functions import *
from pygame.locals import *
from random import *

def main():

    basketLeft = 200;
    basketTop = 550;
    basketwidth = 100;
    basketHeight = 30;
    
    width = 500
    height = 600
    
    # initialize scree
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Catch the Quince')

    FPS = 20
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
    
    Radius = 10
    
    action = 0
    score = 0
    missed = 0
    max_score = 0
    reward = 0
    
    font = pygame.font.Font(None, 30)
    
    circle = pygame.Rect(0, 30, 100, 100)
    rect2 = pygame.Rect(basketLeft,basketTop,basketwidth,basketHeight)
    
    lr = .85
    dr = .99
    epsilon = 1.0
    

    # display some text
    #font = pygame.font.Font(None, 36)
    #text = font.render("Hello from Monty PyGame", 1, (10, 10, 10))
    #textpos = text.get_rect()
    #textpos.centerx = background.get_rect().centerx
    #background.blit(text, textpos)
     
    # blit everything to the screen
    screen.blit(background, (0, 0))
    #pygame.display.flip()

    #move_it = False
    #move_direction = 1
     
  
    # event loop
    while True:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print(epsilon)

               
                #if(rect1.collidepoint((mouseX, mouseY))):
                    #move_it = not move_it
         
        s = State(rect2, Circle(crclCentreX, crclCentreY))
         
        pygame.draw.circle(screen, YELLOW, (crclCentreX, crclCentreY), Radius)
        
        action = get_best_action(s, epsilon)
        s1 = take_action(s, action)
        r0 = calculate_score(s1.rect, s1.circle)
        
        QTable[find_state(s), action] = QTable[find_state(s), action] + lr * (r0 + dr * np.max(QTable[find_state(s1), :]) - QTable[find_state(s), action])
            
        
        rect2 = s1.rect
        pygame.draw.rect(screen, RED, rect2)  # rect(Surface, color, Rect, width=0)
        
        crclCentreY += 10
        
       
        if r0 == -100:
            rect2 = pygame.Rect(basketLeft,basketTop,basketwidth,basketHeight)
            crclCentreY = 10
            crclCentreX = new_circleX()
            missed += 1
            score = 0
        elif r0 == 2:
            score += 1
            if score >= max_score:
                max_score = score
            crclCentreY = 10
            crclCentreX = new_circleX()
        
        
            
        #if move_it:
            #rect1.move_ip(0,move_direction * 5)
            #if not screen.get_rect().contains(rect1):
                #move_direction = move_direction * -1
                #rect1.move_ip(0, move_direction * 5)
         
        #pygame.draw.rect(screen, BLACK, rect1, 1)
        #pygame.draw.rect(screen, (255,255,255, 255), quince_rect, 1)
        #pygame.display.flip()
        
        #s = State(rectangle, Circle(crclCentreX, crclCentreY)
                
        #print(crclCentreX)
            
        #PLAY YOURSELF :)
        keys = pygame.key.get_pressed()
        #if keys[pygame.K_LEFT] and basketLeft > 0:
            #basketLeft -= 50
            #print(basketLeft)
        #if keys[pygame.K_RIGHT] and basketLeft < width-basketwidth:
            #basketLeft += 50
            #print(basketLeft)
        if keys[pygame.K_q] or keys[pygame.K_a]:
            pygame.quit()
            sys.exit()
                
                
        
        
        # circle(Surface, color, pos(x, y), radius, width=0)
        #fruit.move_ip(move_direction * 5, 0)
        
        #quince_rect.move_ip(0, move_direction * 5)
        #screen.blit(quince, quince_rect)
    
        text = font.render('score: ' + str(score), True, (238, 58, 140))  # update the score on the screen
        text1 = font.render('missed: ' + str(missed), True, (238, 58, 140))  # update the score on the screen
        text2 = font.render('max: ' + str(max_score), True, (238, 58, 140))
        screen.blit(text, (width - 120, 10))  # render score
        screen.blit(text1, (width - 280, 10))  # render missed
        screen.blit(text2, (width - 440, 10))  # render max
            
        pygame.display.update()
        clock.tick(FPS)
        
        epsilon = set_epsilon(epsilon)
        
if __name__ == '__main__':
    main()
