from random import *
import random
import pygame as pygame
from definitions import *
from classes import *

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
    
def calculate_score(rect, quince): #30 >= 525
    if quince.top + 20 >= rect.top:
        if rect.left <= quince.left and quince.right <= rect.right:
            return 2
        else:
            #print(rect.left)
            #print(quince.left)
            return -100
    else:
        if rect.left <= quince.left and quince.right <= rect.right:
            return 1
        else:
            return -1
    
def find_state(state):
    
    r = state.rect
    q = state.quince
    
    yled = r.top - q.top
    xled = q.left - r.left
    
    n = (int(str(xled) + str(yled)))
    if n in QDic: # use a dictionary to access the index of the Qtable
        return QDic[n]
    else:
        #print("add entry in QDic")
        if len(QDic):
            maximum = max(QDic, key=QDic.get)
            QDic[n] = QDic[maximum] + 1
        else:
            #print("EMPTY QDic")
            QDic[n] = 1
    return QDic[n]
    
def find_state2(state):
    r = state.rect
    q = state.quince
    
    yled = r.top - q.top
    xled = q.left - r.left
    
    n = (int(str(xled) + str(yled)))
    # use a dictionary to access the index of the Qtable
    if n in QDic2: # use a dictionary to access the index of the Qtable
        return QDic2[n]
    else:
        print(n)
        print("NO")
        return 1

def add_data(reward):
    Data.append(reward)
    #np.insert(Data, Data.size, reward)
   # if len(Data):
    #    maximum = max(Data, key=Data.get)
    #    Data[len(Data) + 1] = reward
    #    print(len(Data))
   # else:
    #    Data[1] = reward
     #   print(len(Data))

def get_best_action(state, epsilon):
    if random.uniform(0, 1) < epsilon:
        action = randrange(3)
    else:
        action = np.argmax(QTable[find_state(state), :])
        #print(action)
    return action
    
def get_best_action2(state):
    return np.argmax(QTable2[find_state2(state), :])

def set_epsilon(epsilon):
    if epsilon > epsilon_min:
        epsilon = epsilon * epsilon_decay
    return epsilon
    
def randomVelocity():
    return (randrange(2) + 1) * 10
    
def switchVelocity(velocity):
    if velocity == 10:
        return 0
    else:
        return 1
