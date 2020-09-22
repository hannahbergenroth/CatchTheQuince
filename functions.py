import random
import pygame as pygame
from definitions import *
from classes import *

basketLeft = 200;
basketTop = 550;
basketwidth = 100;
basketHeight = 30;

def new_state(state,action)
    rect = None
    
    if action == 1 and basketLeft < width - basketwidth: #right
        rect = pygame.Rect(state.left + basketStep, state.top, state.width, state.height)
    elif action == 2 and basketLeft > 0: # left
        rect = pygame.Rect(state.left - basketStep, state.top, state.width, state.height)
    else
        rect = state.rect
        
    circle = s.Circle(state.circleX, state.circleY + circleStep)
    
    return State(rect, circle)
    
def new_circleX
    return circleX = randrange(10) * 55 + 25
    
def find_state(state)
    r = state.rect.left
    cX = state.circle.circleX
    cY = state.circle.circleY
    n = (int(str(r) + str(cX) + str(cY)))
    
    # use a dictionary to access the index of the Qtable
    if n in QDic:
        return QDic[n]
    else:
        if len(QDic):
            maximum = max(QDic, key=QDic.get)
            QDic[n] = QDic[maximum] + 1
        else:
            QDic[n] = 1
    return QDic[n]
    
def get_best_action(state)
    return np.argmax(QTable[find_state(state), :])
 
    
