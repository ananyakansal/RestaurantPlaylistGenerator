import numpy as np
import sys
import pandas as pd
from random import seed
from random import randint
from collections import deque
import math
import random


staticList = []
global queue
queue = deque()


def initQueue():
    global queue
    queue.append(randomNext())
    queue.append(randomNext())
    queue.append(randomNext())
    # print(queue)

def addToQueue():
    global queue
    queue.append(randomNext())

def playQueue(spl=None):
    global queue
    if (spl == None):
        queue.append(randomNext())
    elif splAvg(spl) == None:
        queue.append(randomNext())
    else:
        queue.append(splNext(splAvg(spl)))
    # print(queue)
    return queue.popleft()

def randomNext():
    seed()
    ind = randint(0, len(staticList))
    song = staticList.pop(ind)
    while ('Not Found' in song):
        ind = randint(0, len(staticList))
        song = staticList.pop(ind)
    return song

def splNext(spl):
    ind = gaussian_pick(spl, staticList)
    song = staticList.pop(ind)
    while ('Not Found' in song):
        ind = gaussian_pick(spl, staticList)
        song = staticList.pop(ind)
    return song

def splAvg(songSPL):
    if len(songSPL) ==  0:
        return None
    return sum(songSPL)/len(songSPL)

def gaussian_pick(ave,static_list): # takes in 'ave': spl value and the (length of the) static playlist
    # this generates a gaussian white noise
    mean = 0
    std = 1
    num_samples = 100
    samples = np.random.normal(mean, std, size=num_samples)
    # this adds the spl value to the gaussian white noise
    # the spl is now a range of values centered around the 'ave' value
    samples = samples+ave
    # divide the spl range (-50 to -5) according to the playlist length
    # find the nearest value of the min and max in the spl range, and map the index to the playlist
    ranking = np.linspace(-50,-5,len(static_list))
    def find_nearest(array,value):
        idx = np.searchsorted(array, value, side="left")
        if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
            return idx-1
        else:
            return idx
    #gives range of index
    picks = [find_nearest(ranking,min(samples)),find_nearest(ranking,max(samples))]
    #gives one random index
    onepick = random.randint(picks[0],picks[1]) 
    return(onepick)
    # or return(onepick)

def getQueue():
    temp = []
    temp.append(queue[0])
    temp.append(queue[1])
    temp.append(queue[2])
    return temp

# initStaticLists()
# setStaticList('classical', 'cheerful', 'bright', 'instrumental', 'fast', 'not_dance')
# print(getStaticList())
# print(gaussian_pick(-30, getStaticList()))
# # # print(randomNext())
# initQueue()


