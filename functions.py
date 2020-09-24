from random import *
import random
import pygame as pygame
from definitions import *
from classes import *

basketLeft = 200;
basketTop = 550;
basketwidth = 100;
basketHeight = 30;

def take_action(state,action):
    rect = None
    if action == 1 and state.rect.right < width: # right
        rect = pygame.Rect(state.rect.left + basketStep, state.rect.top, state.rect.width, state.rect.height)
    elif action == 2 and state.rect.left > 0: # left
        rect = pygame.Rect(state.rect.left - basketStep, state.rect.top, state.rect.width, state.rect.height)
    else:
        rect = state.rect
    
    return State(rect, state.circle)
    
def get_rect(rect, action):
    if action == 1 and rect.right < width: # right
        return pygame.Rect(rect.left + basketStep, rect.top, basketwidth, basketHeight)
    elif action == 2 and rect.left > 0: # left
        return pygame.Rect(rect.left - basketStep, rect.top, basketwidth, basketHeight)
    else:
        return rect
    
def new_circleX():
    range = randrange(9) * 55 + 30
    print(range)
    return (range)
    
def calculate_score(rect, circle):
    if circle.circleY >= rect.top:
        if rect.left <= circle.circleX <= rect.right:
            return 2
        else:
            return -100
    else:
        if rect.left <= circle.circleX <= rect.right:  # if the circle'x x position is between the rectangles left and right
            return 1
        else:
            return -1
        
def calculate_score2(rect, circle):
    return 1
    
def find_state(state):
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
    
def get_best_action(state, epsilon):
    if random.uniform(0, 1) < epsilon:
        action = randrange(3)
    else:
        action = np.argmax(QTable[find_state(state), :])
    #if epsilon > epsilon_min:
     #   epsilon *= epsilon_decay
    return action


def set_epsilon(epsilon):
    if epsilon > epsilon_min:
        epsilon = epsilon * epsilon_decay
    return epsilon
