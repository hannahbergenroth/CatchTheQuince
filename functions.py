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
    
    return State(rect, state.quince)
    
def new_circleX():
    return (randrange(9) * 55 + 15)
    
def calculate_score(rect, quince):
    if quince.top + 20 >= rect.top:
        if rect.left <= quince.left and quince.right <= rect.right:
            return 2
        else:
            print(rect.left)
            print(quince.left)
            return -100
    else:
        if rect.left <= quince.left and quince.right <= rect.right:  # if the circle'x x position is between the rectangles left and right
            return 1
        else:
            return -1
    
def find_state(state):
    r = state.rect.left
    cX = state.quince.left
    cY = state.quince.top
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
