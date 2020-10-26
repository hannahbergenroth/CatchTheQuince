import numpy as np
from numpy import *
import ast
import h5py

epsilon_min = 0.01
epsilon_decay = 0.99995

width = 500
height = 600

basketLeft = 200;
basketTop = 525;
basketwidth = 100;
basketHeight = 70;

RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255,215,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

basketStep = 50
circleStep = 30
circleY = 10
circleRadius = 10

file = open('dictionarynTHIS.txt', 'r')
contents = file.read()
QDic2 = ast.literal_eval(contents)
QDic = {}
#Data = array((1))
Data = []

QTable = np.zeros([5000,3]) #number of states (500/10) * (600/60) * (500/100) # 50 * 9 * 9
filename = 'QTableTHIS.h5'
with h5py.File(filename, 'r') as hf:
    data = hf['this'][:]
QTable2 = data
