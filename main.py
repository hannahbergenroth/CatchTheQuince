from classes import State
import pygame, sys, time, random
from definitions import *
from functions import *
from pygame.locals import *
from random import *
import pygame_menu
import h5py
import ast

def change_player(value, difficulty):
    playable = difficulty
    print(playable)
    return difficulty

def game_loop(screen, height, width, player):
    
    filename = 'QTable.h5'
    # initialize scree
    pygame.display.set_caption('Catch the Quince')

    FPS = 20
    clock = pygame.time.Clock()


   
    # fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((WHITE))
  
    #use image as object
    basket = pygame.image.load('basket.png')
    basket = pygame.transform.scale(basket,(100,70))
    rect2 = basket.get_rect()
    rect2.top = 525
    rect2.left = 200
  
    quince = pygame.image.load('quince.png')
    quince = pygame.transform.scale(quince, (40,40))
    quince_rect = quince.get_rect()
    quince_rect.top = 10
    quince_rect.left = new_circleX()
  
    action = 0
    score = 0
    missed = 0
    max_score = 0
  
    font = pygame.font.Font(None, 30)
    
    velocity = 10
  
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
                print(epsilon)
    
        # CHANGE PLAYER - AI, 1 = Play, 2 = Learn
        if player == 1 or player == 2:
            if player == 1:
                epsilon = 0
            #with h5py.File(filename, 'r') as hf:
            #  data = hf['this'][:]
            #QTable = data
            
            #filen = open('dictionaryn.txt', 'r')
            #contents = filen.read()
            #dictionary = ast.literal_eval(contents)
     
            #QDic = ast.literal_eval(contents)
            #filen.close()
            
            s = State(rect2, quince_rect)
            pygame.draw.rect(screen, (255,255,255),  quince_rect, 1)
            if player == 2:
                action = get_best_action(s, epsilon)
            else:
                action = get_best_action2(s)
            s1 = take_action(s, action)
            r0 = calculate_score(s1.rect, s1.quince)
          
            if player == 2:
                QTable[find_state(s), action] = QTable[find_state(s), action] + lr * (r0 + dr * np.max(QTable[find_state(s1), :]) - QTable[find_state(s), action])
              
            rect2 = s1.rect
            pygame.draw.rect(screen, (255,255,255), rect2, 1)  # rect(Surface, color, Rect, width=0)
        
            quince_rect.top += velocity
          
            if r0 == -100:
                rect2 = pygame.Rect(basketLeft,basketTop,basketwidth,basketHeight)
                quince_rect.top = 20
                quince_rect.left = new_circleX()
                velocity = randomVelocity()
                missed += 1
                score = 0
            elif r0 == 2:
                velocity = randomVelocity()
                score += 1
                quince_rect.top = 20
                quince_rect.left = new_circleX()
                if score >= max_score:
                    max_score = score
          
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] or keys[pygame.K_a]:
            # UPDATE QTable and QDic
            with h5py.File('QTableTHIS.h5', 'w') as hf:
               hf.create_dataset('this', data = QTable )
            f = open('dictionarynTHIS.txt', 'w')
            f.write(str(QDic))
            f.close()
            pygame.quit()
            sys.exit()
        
        #PLAY YOURSELF :) CHANGE PLAYER
        if player == 0:
            pygame.draw.rect(screen, (255,255,255),  quince_rect, 1)
            pygame.draw.rect(screen, (255,255,255), rect2, 1)
            quince_rect.top += velocity
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and rect2.left > 0:
                rect2.left -= 50
                print(rect2.left)
            if keys[pygame.K_RIGHT] and rect2.left < width-basketwidth:
                rect2.left += 50
                print(rect2.left)
            if keys[pygame.K_q]:
                pygame.quit()
                sys.exit()
            if quince_rect.top + 20 >= rect2.top:
                if rect2.left <= quince_rect.left and quince_rect.right <= rect2.right:
                    velocity = randomVelocity()
                    score += 1
                    quince_rect.top = 20
                    quince_rect.left = new_circleX()
                    if score >= max_score:
                        max_score = score
                else:
                    velocity = randomVelocity()
                    rect2 = pygame.Rect(basketLeft,basketTop,basketwidth,basketHeight)
                    quince_rect.top = 20
                    quince_rect.left = new_circleX()
                    missed += 1
                    score = 0
      
        screen.blit(quince, quince_rect)
        screen.blit(basket, rect2)
  
        text = font.render('score: ' + str(score), True, (238, 58, 140))  # update the score on the screen
        text1 = font.render('missed: ' + str(missed), True, (238, 58, 140))  # update the score on the screen
        text2 = font.render('max: ' + str(max_score), True, (238, 58, 140))
        screen.blit(text, (width - 120, 10))  # render score
        screen.blit(text1, (width - 280, 10))  # render missed
        screen.blit(text2, (width - 440, 10))  # render max
          
        pygame.display.update()
        clock.tick(FPS)
      
        if player == 2:
            epsilon = set_epsilon(epsilon)

def main():
    pygame.init()
    width = 500
    height = 600
    you_play = 0
    ai_play = 1
    ai_learn = 2
    
    # initialize scree
    screen = pygame.display.set_mode((width, height))
    menu = pygame_menu.Menu(500, 500, 'Welcome', theme=pygame_menu.themes.THEME_DARK)
    menu.add_button('Learn AI play', game_loop, screen, height, width, ai_learn)
    menu.add_button('Let AI play', game_loop, screen, height, width, ai_play)
    menu.add_button('Play yourself', game_loop, screen, height, width, you_play)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)
    
if __name__ == '__main__':
    main()
