import numpy as np

epsilon_min = 0.01
epsilon_decay = 0.9995

width = 500
height = 600

RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255,215,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

basketStep = 50
circleStep = 30
circleY = 10
circleRadius = 10

QDic = {}

QTable = np.zeros([5000,3]) #number of states (500/10) * (600/60) * (500/100)
