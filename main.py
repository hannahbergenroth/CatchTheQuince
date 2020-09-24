from classes import State, Circle
import pygame, sys, time, random
from definitions import *
from functions import *
from pygame.locals import *
from random import *
import pygame_menu

def change_player(value, difficulty):
    print(value)
    print(difficulty)
    pass
    
def start_the_game():
    print("woooo")
    pass

def main():

    basketLeft = 200;
    basketTop = 525;
    basketwidth = 100;
    basketHeight = 70;
    
    width = 500
    height = 600
    
    # initialize scree
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Catch the Quince')
    
    menu = pygame_menu.Menu(500, 500, 'Welcome', theme=pygame_menu.themes.THEME_DARK)
    menu.add_text_input('Name :', default='John Doe')
    menu.add_selector('Play :', [('You', 1), ('IT', 2)], onchange=change_player)
    menu.add_button('Play', start_the_game)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

    FPS = 20
    clock = pygame.time.Clock()
     
    # fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((WHITE))
    
    basket = pygame.image.load('basket.png')
    basket = pygame.transform.scale(basket,(100,70))
    rect2 = basket.get_rect()
    rect2.top = 525
    #use image as object
    quince = pygame.image.load('quince.png')
    quince = pygame.transform.scale(quince, (50,40))
    quince_rect = quince.get_rect()

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
    
    lr = .85
    dr = .99
    epsilon = 1.0
     
    # blit everything to the screen
    screen.blit(background, (0, 0))
    #pygame.display.flip()
     
  
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
        pygame.draw.rect(screen, (255,255,255), rect2, 1)  # rect(Surface, color, Rect, width=0)
        
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
         
        #pygame.draw.rect(screen, BLACK, rect1, 1)
        #pygame.draw.rect(screen, (255,0,0), basket_rect, 0)
        #pygame.display.flip()
        
        #s = State(rectangle, Circle(crclCentreX, crclCentreY)
                
        #print(crclCentreX)
            
        #PLAY YOURSELF :)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] or keys[pygame.K_a]:
            pygame.quit()
            sys.exit()
        
        # circle(Surface, color, pos(x, y), radius, width=0)
        #fruit.move_ip(move_direction * 5, 0)
        
     
        screen.blit(basket, rect2)
    
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
