import numpy as np
import sys
import pandas as pd
from random import seed
from random import randint
from collections import deque

list1 = []
staticList = []
global queue
queue = deque()

def initStaticLists():
    df = pd.read_csv('out.csv')
    alldata = df.values.tolist()
    # classical cheerful bright instrumental fast not_dance 281
    global list1
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 11:
                if alldata[i][27] == 15:
                    if alldata[i][28] == 17:
                        if alldata[i][29] == 19:
                            if alldata[i][30] == 1:
                                list1.append(alldata[i][24])

def getStaticList():
    global staticList
    return staticList

def setStaticList(genre=None, mood=None, timbre=None, instrumental=None, tempo=None, dance=None):
    if genre is 'classical' and mood is 'cheerful' and timbre is 'bright' and instrumental is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
        global list1
        global staticList
        staticList = list1

def initQueue():
    global queue
    queue.append(randomNext())
    queue.append(randomNext())
    queue.append(randomNext())
    print(queue)

def addToQueue():
    global queue
    queue.append(randomNext())

def randomNext():
    seed()
    ind = randint(0, len(staticList))
    song = staticList.pop(ind)
    while ('Not Found' in song):
        ind = randint(0, len(staticList))
        song = staticList.pop(ind)
    return song

# initStaticLists()
# setStaticList('classical', 'cheerful', 'bright', 'instrumental', 'fast', 'not_dance')
# # print(getStaticList())
# # print(randomNext())
# initQueue()


