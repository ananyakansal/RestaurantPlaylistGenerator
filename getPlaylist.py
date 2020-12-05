import numpy as np
import sys
import pandas as pd
from random import seed
from random import randint
from collections import deque
import math
import random

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []
list13 = []
list14 = []
list15 = []
list16 = []
list17 = []
list18 = []
list19 = []
list20 = []
list21 = []
list22 = []
list23 = []
list24 = []
list25 = []
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
    # classical cheerful bright voice fast not_dance 314
    global list2
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 11:
                if alldata[i][27] == 15:
                    if alldata[i][28] == 18:
                        if alldata[i][29] == 19:
                            if alldata[i][30] == 1:
                                list2.append(alldata[i][24])
    global list3
    # classical cheerful bright voice slow notdance 165
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 11:
                if alldata[i][27] == 15:
                    if alldata[i][28] == 18:
                        if alldata[i][29] == 20:
                            if alldata[i][30] == 1:
                                list3.append(alldata[i][24])
    global list4
    # classical cheerful dark instrumental fast notdance 150
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 11:
                if alldata[i][27] == 16:
                    if alldata[i][28] == 17:
                        if alldata[i][29] == 19:
                            if alldata[i][30] == 1:
                                list4.append(alldata[i][24])
    global list5
    # classical bittersweet bright instrumental fast notdance 717
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 12:
                if alldata[i][27] == 15:
                    if alldata[i][28] == 17:
                        if alldata[i][29] == 19:
                            if alldata[i][30] == 1:
                                list5.append(alldata[i][24])
    global list6
    # classical bittersweet bright instrumental slow not_dance 230
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 12:
                if alldata[i][27] == 15:
                    if alldata[i][28] == 17:
                        if alldata[i][29] == 20:
                            if alldata[i][30] == 1:
                                list6.append(alldata[i][24])
    global list7
    # classical bittersweet bright voice fast not_dance 243
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 12:
                if alldata[i][27] == 15:
                    if alldata[i][28] == 18:
                        if alldata[i][29] == 19:
                            if alldata[i][30] == 1:
                                list7.append(alldata[i][24])
    global list8
    # classical bittersweet bright voice slow not_dance 243
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 12:
                if alldata[i][27] == 15:
                    if alldata[i][28] == 18:
                        if alldata[i][29] == 20:
                            if alldata[i][30] == 1:
                                list8.append(alldata[i][24])
    global list9
    # classical bittersweet dark instrumental fast not_dance 828
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 12:
                if alldata[i][27] == 16:
                    if alldata[i][28] == 17:
                        if alldata[i][29] == 19:
                            if alldata[i][30] == 1:
                                list9.append(alldata[i][24])
    global list10
    # classical bittersweet dark instrumental slow not_dance 312
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 12:
                if alldata[i][27] == 16:
                    if alldata[i][28] == 17:
                        if alldata[i][29] == 20:
                            if alldata[i][30] == 1:
                                list10.append(alldata[i][24])
    global list11
    # classical bittersweet dark voice fast not_dance 232
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 12:
                if alldata[i][27] == 16:
                    if alldata[i][28] == 18:
                        if alldata[i][29] == 19:
                            if alldata[i][30] == 1:
                                list11.append(alldata[i][24])
    global list12
    # classical bittersweet dark voice slow not_dance 79
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 12:
                if alldata[i][27] == 16:
                    if alldata[i][28] == 18:
                        if alldata[i][29] == 20:
                            if alldata[i][30] == 1:
                                list12.append(alldata[i][24])
    global list13
    # classical humorous not_dance 317
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 13:
                if alldata[i][30] == 1:
                    list13.append(alldata[i][24])
    global list14
    # classical agreesive slow not_dance 284
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 14:
                if alldata[i][29] == 20:
                    if alldata[i][30] == 1:
                        list14.append(alldata[i][24])
    global list15
    # classical agreesive bright instrumental fast not_dance 468
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 14:
                if alldata[i][27] == 15:
                    if alldata[i][28] == 17:
                        if alldata[i][29] == 19:
                            if alldata[i][30] == 1:
                                list15.append(alldata[i][24])
    global list16
    # classical agreesive bright voice fast not_dance 128
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 14:
                if alldata[i][27] == 15:
                    if alldata[i][28] == 18:
                        if alldata[i][29] == 19:
                            if alldata[i][30] == 1:
                                list16.append(alldata[i][24])
    global list17
    # classical agreesive dark instrumental fast not_dance 655
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 14:
                if alldata[i][27] == 16:
                    if alldata[i][28] == 17:
                        if alldata[i][29] == 19:
                            if alldata[i][30] == 1:
                                list17.append(alldata[i][24])
    global list18
    # classical agreesive dark voice fast not_dance 133
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][26] == 14:
                if alldata[i][27] == 16:
                    if alldata[i][28] == 18:
                        if alldata[i][29] == 19:
                            if alldata[i][30] == 1:
                                list18.append(alldata[i][24])
    global list19
    # classical danceable 266
    for i in range(0, len(alldata)):
        if alldata[i][25] == 2:
            if alldata[i][30] == 0:
                list19.append(alldata[i][24])
    global list20
    # dance notdanceable 681 who wouldn't love that
    for i in range(0, len(alldata)):
        if alldata[i][25] == 3:
            if alldata[i][30] == 1:
                list20.append(alldata[i][24])
    global list21
    # dance slow danceable 325
    for i in range(0, len(alldata)):
        if alldata[i][25] == 3:
            if alldata[i][29] == 20:
                if alldata[i][30] == 0:
                    list21.append(alldata[i][24])
    global list22
    # dance not_aggressive instrumental fast danceable 115
    for i in range(0, len(alldata)):
        if alldata[i][25] == 3:
            if alldata[i][28] == 17:
                if alldata[i][29] == 19:
                    if alldata[i][30] == 0:
                        if alldata[i][26] != 14:
                            list22.append(alldata[i][24])
    global list23
    # dance aggressive bright instrumental fast danceable 388
    for i in range(0, len(alldata)):
        if alldata[i][25] == 3:
            if alldata[i][26] == 14:
                if alldata[i][27] == 15:
                    if alldata[i][28] == 17:
                        if alldata[i][29] == 19:
                            if alldata[i][30] == 0:
                                list23.append(alldata[i][24])
    global list24
    # dance aggressive bright voice fast danceable 252
    for i in range(0, len(alldata)):
        if alldata[i][25] == 3:
            if alldata[i][26] == 14:
                if alldata[i][27] == 15:
                    if alldata[i][28] == 18:
                        if alldata[i][29] == 19:
                            if alldata[i][30] == 0:
                                list24.append(alldata[i][24])
    global list25
    # dance aggressive dark instrumental fast danceable 667
    for i in range(0, len(alldata)):
        if alldata[i][25] == 3:
            if alldata[i][26] == 14:
                if alldata[i][27] == 16:
                    if alldata[i][28] == 17:
                        if alldata[i][29] == 19:
                            if alldata[i][30] == 0:
                                list25.append(alldata[i][24])
    
def getStaticList():
    global staticList
    return staticList

def setStaticList(genre=None, mood=None, timbre=None, instrumental=None, tempo=None, dance=None):
    df = pd.read_csv('out.csv')
    alldata = df.values.tolist()
    if genre is 'classical' and mood is 'cheerful' and timbre is 'bright' and instrumental is 'instrumental' and tempo is 'fast' and dance is 'not_dance':
        global list1
        for i in range(0, len(alldata)):
            if alldata[i][25] == 2:
                if alldata[i][26] == 11:
                    if alldata[i][27] == 15:
                        if alldata[i][28] == 17:
                            if alldata[i][29] == 19:
                                if alldata[i][30] == 1:
                                    list1.append(alldata[i][24])
        global staticList
        staticList = list1

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


